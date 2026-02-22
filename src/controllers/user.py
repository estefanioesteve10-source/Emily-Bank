import sqlite3
import random

def gerar_iban():
    # Prefixo fixo solicitado + resto aleatório (11 dígitos para completar 25 caracteres padrão)
    prefixo = "PT50 0001 0000 20"
    resto = ''.join([str(random.randint(0, 9)) for _ in range(11)])
    return prefixo + resto

def cadastro():
    nome = input('Digite o teu nome: ')
    iban = gerar_iban()

    conn = sqlite3.connect('../Emily_Banc.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO clientes (nome, iban) VALUES (?, ?)', (nome, iban))
        conn.commit()
        print(f"\nConta criada! Nome: {nome}")
        print(f"Seu IBAN oficial: {iban}")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar: {e}")
    conn.close()