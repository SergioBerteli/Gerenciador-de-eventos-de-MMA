import mysql.connector, time

print("Conectando à base de dados...")
while(1):
    try:
        connection = mysql.connector.connect(
            user='root', password="", host='localhost', database='test')
        break
    except:
        print("Erro ao tentar conectar com a base de dados, tentando novamente em 5 segundos!")
        time.sleep(5)
cursor = connection.cursor()
cursor.execute('SELECT * FROM Lutadores')
livros = cursor.fetchall()
print(livros)
connection.close()