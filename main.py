import sqlite3
import random

def gerar_iban():
    # Prefixo fixo solicitado + resto aleatório (11 dígitos para completar 25 caracteres padrão)
    prefixo = "PT50 0001 0000 20"
    resto = ''.join([str(random.randint(0, 9)) for _ in range(11)])
    return prefixo + resto

def iniciar_banco():
    conn = sqlite3.connect('Emily_Banc.db')
    cursor = conn.cursor()
    # IBAN agora é a PRIMARY KEY
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            iban TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            saldo REAL DEFAULT 0,
            num_transferencias INTEGER DEFAULT 0,
            num_depositos INTEGER DEFAULT 0,
            num_levantamentos INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def cadastro():
    nome = input('Digite o teu nome: ')
    iban = gerar_iban()
    
    conn = sqlite3.connect('Emily_Banc.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO clientes (nome, iban) VALUES (?, ?)', (nome, iban))
        conn.commit()
        print(f"\nConta criada! Nome: {nome}")
        print(f"Seu IBAN oficial: {iban}")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar: {e}")
    conn.close()


def levantamento():
    print("\n--- Área de Levantamento ---")
    iban_origem = input('Digite o SEU IBAN: ')
    valor = float(input('Valor a levantar: '))

    conn = sqlite3.connect('Emily_Banc.db')
    cursor = conn.cursor()

    try:
        # 1. Verifica saldo do remetente
        cursor.execute('SELECT saldo FROM clientes WHERE iban = ?', (iban_origem,))
        res = cursor.fetchone()
        
        if not res or res[0] < valor:
            print("Saldo insuficiente ou IBAN de origem inválido.")
            return

        # Início da Transação Atômica
        # Retira da origem
        cursor.execute('UPDATE clientes SET saldo = saldo - ?, num_transferencias = num_transferencias + 1 WHERE iban = ?', (valor, iban_origem))
       
        conn.commit()
        print(f"Levantamento de {valor}€ realizada com sucesso!")

    except Exception as e:
        conn.rollback() # Cancela tudo se der erro
        print(f"Erro na operação: {e}")
    finally:
        conn.close()


def transferencia():
    print("\n--- Área de Transferência ---")
    iban_origem = input('Digite o SEU IBAN: ')
    iban_destino = input('Digite o IBAN do DESTINATÁRIO: ')
    valor = float(input('Valor a transferir: '))

    conn = sqlite3.connect('Emily_Banc.db')
    cursor = conn.cursor()

    try:
        # 1. Verifica saldo do remetente
        cursor.execute('SELECT saldo FROM clientes WHERE iban = ?', (iban_origem,))
        res = cursor.fetchone()
        
        if not res or res[0] < valor:
            print("O Saldo é insuficiente ou IBAN de origem inválido.")
            return

        # Início da Transação Atômica
        # Retira da origem
        cursor.execute('UPDATE clientes SET saldo = saldo - ?, num_transferencias = num_transferencias + 1 WHERE iban = ?', (valor, iban_origem))
        
        # Adiciona no destino
        cursor.execute('UPDATE clientes SET saldo = saldo + ? WHERE iban = ?', (valor, iban_destino))
        
        if cursor.rowcount == 0:
            raise Exception("O Destinatário não foi encontrado.")

        conn.commit()
        print(f"A Transferência de {valor}€ realizada com sucesso!")

    except Exception as e:
        conn.rollback() # Cancela tudo se der erro
        print(f"Erro na operação: {e}")
    finally:
        conn.close()

# Reaproveitando as funções anteriores com a nova PK
def deposit():
    iban = input('Digite o IBAN para depósito: ')
    valor = float(input('Quanto quer depositar? '))
    conn = sqlite3.connect('Emily_Banc.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE clientes SET saldo = saldo + ?, num_depositos = num_depositos + 1 WHERE iban = ?', (valor, iban))
    if cursor.rowcount > 0:
        conn.commit()
        print("Depósito concluído.")
    else:
        print("IBAN não encontrado.")
    conn.close()

def consulta():
    iban = input('Digite o IBAN para consulta: ')
    conn = sqlite3.connect('Emily_Banc.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes WHERE iban = ?', (iban,))
    row = cursor.fetchone()
    if row:
        print(f"\n--- Detalhes da Conta ---")
        print(f"Titular: {row[1]} | Saldo: {row[2]}€")
        print(f"IBAN: {row[0]}")
        print(f"Histórico: {row[3]} Transf | {row[4]} Dep | {row[5]} Lev")
    else:
        print("Conta inexistente.")
    conn.close()

def logica():
    iniciar_banco()
    while True:
        print("\n1-Criar Conta | 2-Deposito | 3-Levantamento | 4-Transferência | 5-Consulta | 6-Sair", flush=True)
        opt = input('Escolha: ')
        if opt == '1': cadastro()
        elif opt == '2': deposit()
        elif opt == '3': levantamento()
        elif opt == '4': transferencia()
        elif opt == '5': consulta()
        elif opt == '6': break

if __name__ == "__main__":
    logica()
