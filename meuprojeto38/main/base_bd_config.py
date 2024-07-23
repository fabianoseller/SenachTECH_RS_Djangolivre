import mysql.connector
from mysql.connector import errorcode
from contextlib import contextmanager
import logging

def conecta_no_banco_de_dados():
    try:
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )
        print("Conexão estabelecida com sucesso!")
        return cnx
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        raise

def criar_banco_de_dados():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )
        
        cursor = connection.cursor()
        
        cursor.execute('CREATE DATABASE IF NOT EXISTS taranbanco;')
        cursor.execute('USE taranbanco;')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes_tarantino (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                ano_lancamento INT NOT NULL,
                onde_assistir VARCHAR(255) NOT NULL,
                elenco TEXT NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                nome VARCHAR(255),
                email VARCHAR(255)
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_filmes (
                usuario_id INT NOT NULL,
                filme_id INT NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (usuario_id, filme_id),
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
                FOREIGN KEY (filme_id) REFERENCES filmes_tarantino(id) ON DELETE CASCADE
            );
        ''')

        connection.commit()
        print('Banco de dados e tabelas criados com sucesso!')
    except mysql.connector.Error as err:
        print("Erro ao criar o banco de dados ou tabelas:", err)
        raise
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

@contextmanager
def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='taranbanco'
        )
        yield connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            criar_banco_de_dados()
            connection = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='taranbanco'
            )
            yield connection
        else:
            logging.error(f"Erro de conexão com o banco de dados: {err}")
            raise
    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    criar_banco_de_dados()
    print("Script de criação do banco de dados executado com sucesso!")
