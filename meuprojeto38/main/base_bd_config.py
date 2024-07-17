import mysql.connector

def conecta_no_banco_de_dados():
    cnx = mysql.connector.connect(host='127.0.0.1',user='root',password='')

def criar_banco_de_dados():
    conectacao = None
    cursor = None
    try:
        conectacao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )
        
        cursor = conectacao.cursor()
        
        cursor.execute('CREATE DATABASE IF NOT EXISTS jamiefoxx;')
        cursor.execute('USE jamiefoxx;')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contatos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                mensagem TEXT NOT NULL
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

        # Criar a tabela user_contatos com as relações especificadas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_contatos (
                usuario_id INT NOT NULL,
                contato_id INT NOT NULL,
                situacao VARCHAR(255) NOT NULL,
                PRIMARY KEY (usuario_id, contato_id),
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
                FOREIGN KEY (contato_id) REFERENCES contatos(id) ON DELETE CASCADE
            );
        ''')

        conectacao.commit()
        print('Banco de dados e tabelas criados com sucesso!')
    except mysql.connector.Error as err:
        print("Erro ao criar o banco de dados ou tabelas:", err)
        raise
    finally:
        if cursor:
            cursor.close()
        if conectacao and conectacao.is_connected():
            conectacao.close()


            
@contextmanager
def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='pythonbas'
        )
        yield connection
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            criar_banco_de_dados()
            connection = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='pythonbas'
            )
            yield connection
        else:
            logging.error(f"Erro de conexão com o banco de dados: {err}")
            raise
    finally:
        if connection and connection.is_connected():
            connection.close()

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
        cursor.execute('CREATE DATABASE IF NOT EXISTS pythonbas;')
        cursor.execute('USE pythonbas;')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contatos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                mensagem TEXT NOT NULL
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_contatos (
                users_id INT NOT NULL,
                contatos_id INT NOT NULL,
                situacao VARCHAR(255) NOT NULL,
                PRIMARY KEY (contatos_id, users_id),
                FOREIGN KEY (users_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (contatos_id) REFERENCES contatos(id) ON DELETE CASCADE
            );
        ''')
        connection.commit()
    except mysql.connector.Error as err:
        logging.error(f"Erro ao criar o banco de dados ou tabelas: {err}")
        raise
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

