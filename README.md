# Emily-Bank
# 🏦 Emily Banc - Sistema de Backend Bancário

O **Emily Banc** é um sistema de gerenciamento de contas bancárias desenvolvido em Python e SQLite. Ele permite o cadastro de clientes, depósitos, levantamentos e transferências seguras entre contas utilizando o IBAN como chave primária.



## 🚀 Funcionalidades

- **Cadastro de Clientes**: Gera automaticamente um IBAN português (PT50...).
- **Gestão Financeira**: Depósitos e levantamentos com atualização em tempo real.
- **Transferências Seguras**: Lógica de transação SQL (Atomicidade) para garantir que o dinheiro chegue ao destino.
- **Módulo Administrativo**: Script separado para visualização de métricas e auditoria de todos os clientes.
- **Persistência de Dados**: Banco de dados relacional SQLite.

## 🛠️ Tecnologias Utilizadas

* **Linguagem**: Python 3.x
* **Banco de Dados**: SQLite3
* **Interface**: Linha de Comando (CLI)

## 📁 Estrutura do Projeto

* `main.py`: O sistema principal para uso dos clientes.
* `admin.py`: Painel de visualização para administradores.
* `Emily_Banc.db`: Arquivo do banco de dados (gerado automaticamente).

## 🔧 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/estefanioesteve10-source/Emily-Bank.git
2
