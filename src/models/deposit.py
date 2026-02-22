import sqlite3

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