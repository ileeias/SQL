import psycopg2

conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='1234',
        host='127.0.0.1',
        port='5432'
)
def insertPint(num):
    for i in range(num):
        name = input('Впишите имя картины _ ')
        author = input('Впишите id художника _ ')
        cur.execute(f"INSERT INTO paintings(name, author_id) VALUES ('{name}', {author});")
        conn.commit()
    print("Картины добавленны.")

cur = conn.cursor()
cur.execute("SELECT id, name, surname FROM authors")
authors = cur.fetchall()
for i in range(len(authors)):
    print(f"{authors[i][0]} - {authors[i][1]} {authors[i][2]}")

new_painting = int(input('Сколько новых картин вы хотите добавить? _ '))
insertPint(new_painting)

cur.close()
conn.close()