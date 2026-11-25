import os
import mysql.connector

try:
    db_user = os.environ['DB_USER']
    db_password = os.environ['DB_PASSWORD']
except KeyError as erro:
    raise RuntimeError(f"Erro: A variável de ambiente {erro} não foi definida no sistema.")

connection = mysql.connector.connect(
    host=os.getenv('DB_HOST', '127.0.0.1'),
    user=db_user,
    password=db_password,
    database='teste_db'
)

cursor = connection.cursor()

# CREATE
nome_produto = 'todynho'
valor = 3
comando = 'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)'
dados = (nome_produto, valor)

cursor.execute(comando, dados)
connection.commit() # Salva a inserção no banco

# READ (Para ler os dados após inserir, faça o SELECT antes do fetchall)
cursor.execute('SELECT * FROM vendas')
resultado = cursor.fetchall()
print(resultado)

cursor.close()
connection.close()
