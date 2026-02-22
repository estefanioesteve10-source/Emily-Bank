import sqlite3

def transferencia():
    print("\n--- Área de Transferência ---")
    iban_origem = input('Digite o SEU IBAN: ')
    iban_destino = input('Digite o IBAN do DESTINATÁRIO: ')
    valor = float(input('Valor a transferir: '))

    conn = sqlite3.connect('../Emily_Banc.db')
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