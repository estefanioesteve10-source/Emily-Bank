import sqlite3
from src.controllers.user import cadastro
from src.models.tranf import transferencia
from src.models.saque import levantamento
from src.models.consult import consulta
from src.models.deposit import deposit


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
