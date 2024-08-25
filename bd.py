import sqlite3

# Função para criar a tabela de senhas (se não existir)
def create_database():
    conn = sqlite3.connect('database/passwords.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar senha no banco de dados
def add_password_to_db(password):
    conn = sqlite3.connect('database/passwords.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO passwords (password) VALUES (?)', (password,))
    conn.commit()
    conn.close()
