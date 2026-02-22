import sqlite3


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