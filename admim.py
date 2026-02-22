import sqlite3

def conectar():
    return sqlite3.connect('Emily_Banc.db')

def painel_admin():
    print("\n" + "="*95) # adicionar qubra de linha e '=' 95 vez
    print(f"{'PAINEL DE ADMINISTRAÇÃO - EMILY BANC':^95}") # centralizar horizontalmente
    print("="*95)
    
    conn = conectar()
    cursor = conn.cursor()
    
    try:
        # Seleciona exatamente as colunas que você pediu
        cursor.execute('''
            SELECT nome, iban, saldo, num_transferencias, num_depositos, num_levantamentos 
            FROM clientes
        ''')
        clientes = cursor.fetchall()
        
        if not clientes:
            print(f"{'Nenhum cliente cadastrado no sistema.':^95}")
        else:
            # Cabeçalho da tabela
            header = f"{'NOME':<20} | {'IBAN':<28} | {'SALDO':<12} | {'TRANSF.':<8} | {'DEP/LEV':<10}"
            print(header)
            print("-" * 95)
            
            for c in clientes:
                nome, iban, saldo, transf, dep, lev = c
                # Formatação: nome (20 chars), iban (28 chars), saldo com 2 casas decimais
                info = f"{nome[:20]:<20} | {iban:<28} | {saldo:>10.2f}€ | {transf:^8} | {dep}/{lev}"
                print(info)
                
        # Resumo total do banco
        cursor.execute('SELECT SUM(saldo), COUNT(*) FROM clientes')
        total_banco, total_users = cursor.fetchone()
        
        print("-" * 95)
        print(f"RESUMO: {total_users} Clientes | Total em Custódia: {total_banco if total_banco else 0.0:.2f}€")
        
    except sqlite3.OperationalError:
        print("Erro: O banco de dados ainda não foi criado ou a tabela não existe")
    finally:
        conn.close()
        print("="*95 + "\n")

if __name__ == "__main__":
    painel_admin()
    input("Pressione Enter para sair...")
