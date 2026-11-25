import mysql.connector

connection = mysql.connector.connect(
    host='oculto para o github',
    user='oculto para o github',
    password='oculto para o github',
    database='oculto para o github'
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
    