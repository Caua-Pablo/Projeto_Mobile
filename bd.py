import mysql.connector
from mysql.connector import Error

class MySQLDatabase:
    def __init__(self, host, username, password, database):
        self._host = "localhost"
        self._username = "root"
        self._password = "root"
        self._database = "test"
        self.conn = None

    def connect(self):
        """Estabelece a conexão com o banco de dados MySQL."""
        try:
            self.conn = mysql.connector.connect(
                host=self._host,
                user=self._username,
                password=self._password,
                database=self._database
            )
            if self.conn.is_connected():
                print("Conexão bem-sucedida ao MySQL.")
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            self.conn = None

    def disconnect(self):
        """Fecha a conexão com o banco de dados."""
        if self.conn is not None and self.conn.is_connected():
            self.conn.close()
            print("Conexão com o MySQL encerrada.")

    def execute_query(self, query):
        """Executa uma query SQL no banco de dados."""
        if self.conn is None or not self.conn.is_connected():
            print("Nenhuma conexão ativa com o MySQL.")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            print("Query executada com sucesso.")
        except Error as e:
            print(f"Erro ao executar query: {e}")
        finally:
            cursor.close()

    def fetch_data(self, query):
        """Executa uma query de SELECT e retorna os dados."""
        if self.conn is None or not self.conn.is_connected():
            print("Nenhuma conexão ativa com o MySQL.")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None
        finally:
            cursor.close()

# Exemplo de uso
if __name__ == "__main__":
    db = MySQLDatabase("localhost", "root", "root", "test")
    db.connect()

    # Executa uma query de exemplo
    db.execute_query("CREATE TABLE IF NOT EXISTS teste (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))")
    
    # Insere dados
    db.execute_query("INSERT INTO teste VALUES ('Ferramenta A')")

    # Busca os dados
    result = db.fetch_data("SELECT * FROM teste")
    for row in result:
        print(row)

    # Desconecta
    db.disconnect()