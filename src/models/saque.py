import sqlite3

def levantamento():
    print("\n--- Área de Levantamento ---")
    iban_origem = input('Digite o SEU IBAN: ')
    valor = float(input('Valor a levantar: '))

    conn = sqlite3.connect('../Emily_Banc.db')
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