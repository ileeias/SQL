# connect = psycopg2.connect(
#     dbname='just_code_db',  # Имя Базы Данных
#     user='justcode',  # Юзернейм
#     password='1234',  # Пароль
#     host='127.0.0.1',  # Адрес постгреса (127.0.0.1 -> localhost)
#     port='5432'  # Порт
# )
import psycopg2

'''
connect = psycopg2.connect(
    dbname = 'postgres',
    user = 'justcode',
    password = '1234',
    host = '127.0.0.1',
    port = '5432'
)

# print(cursor.fetchall())
# cursor.close()
# connect.close()
cursor = connect.cursor()
cursor.execute('SELECT * FROM students')
data = cursor.fetchall()
students(name, surname, year) VALUES('{name}', '{surname}', '{year}')")
cursor = connect.cursor()

# cursor.execute(f"INSERT INTO students(name, surname, year) VALUES('{name}', '{surname}', {year})")
# connect.commit()  # commit -> CREATE, UPDATE, INSERT, DELETE, DROP, ... -> Подтверждение действия
#
# cursor.close()
# connect.close()

name = input('WHAT YOUR NAME?')
surname = input("WHAT YOUR SURNAME?")
year = int(input("YEAR?"))
cursor = connect.cursor()
cursor.execute(f"INSERT INTO students(name, surname, year) VALUES('{name}', '{surname}', {year})")
connect.commit()
cursor.close()
connect.close()
'''
# import psycopg2
#
# conn = psycopg2.connect(
#     dbname = 'postgres',
#     user = 'postgres',
#     password = '1234',
#     host = 'localhost',
#     port = '5432'
# )
# # cursor = conn.cursor()
# # cursor.execute("SELECT id, name FROM genres")  # execute(<SQL>) - Позволяет выполнить sql команду <SQL>
# # data = cursor.fetchall()
# # print("Введите название жанра, который хотите добавить")
# # new_genre = input()
# # cursor.execute(f"INSERT INTO genres(name) VALUES('{new_genre}')")
# # conn.commit()  # Подтверждение на действия до этой строки
# cursor = conn.cursor()
# name_dir = input('Введите имя режисёра')
# surname_dir = input('Введите фамилию режисёра')
# cursor.execute(f"INSERT INTO directors(name, surname) VALUES('{name_dir}', '{surname_dir}')")
# conn.commit()
# cursor.execute("SELECT id, name FROM genres")
# data = cursor.fetchall()
# print(data)
# name_film = input('Name film')
# year_film = int(input('Year film'))
# genre_id = int(input('id genre'))
# director_id = int(input('id director'))
# cursor.execute(f"INSERT INTO films(name, year, genre_id, director_id) "
#                f"VALUES('{name_film}', {year_film}, {genre_id}, {director_id})")
# conn.commit()

# import psycopg2
# from telebot import TeleBot
#
# bot = TeleBot("7375162409:AAHYUQGq45SR8VdeokV--IiX272UrzBO8t4")
#
# @bot.message_handler(commands=['products_brands'])
# def getProducts_brands(message):
#     conn = psycopg2.connect(
#         dbname='postgres',
#         user='postgres',
#         password='1234',
#         host='127.0.0.1',
#         port='5432'
#     )
#     id = (message.text).split('/products_brands ')[-1]
#     cur = conn.cursor()
#     if id.isalnum():
#         cur.execute(f'SELECT name FROM brands WHERE id = {id}')
#         brands = cur.fetchall()
#         cur.execute(f'SELECT * FROM products WHERE brand_id = {id}')
#         bot.send_message(message.chat.id, f"You have chosen {brands[0][0]}")
#     else:
#         cur.execute(f'SELECT * FROM products')
#         bot.send_message(message.chat.id, f"You have't chosen brand!")
#
#     result = cur.fetchall()
#     text = ''
#     for i in range(len(result)):
#         text += f'<strong>{str(result[i][1])}</strong>: <i>{str(result[i][2])}</i>\n Price: {str(result[i][3])}$\n Quantity: {str(result[i][5])}\n\n'
#     bot.send_message(message.chat.id, text, parse_mode='HTML')
#     cur.close()
#     conn.close()
#
# @bot.message_handler(commands=['categories'])
# def getCategories(message):
#     conn = psycopg2.connect(
#         dbname='postgres',
#         user='postgres',
#         password='1234',
#         host='127.0.0.1',
#         port='5432'
#     )
#     cur = conn.cursor()
#     cur.execute('SELECT id, name FROM categories')
#     categories = cur.fetchall()
#     text = ''
#     for i in range(len(categories)):
#         text += str(categories[i][0]) + ' - ' + str(categories[i][1]) + '\n'
#     bot.send_message(message.chat.id, text)
#     cur.close()
#     conn.close()
#
# @bot.message_handler(commands=['brands'])
# def getBrands(message):
#     conn = psycopg2.connect(
#         dbname='postgres',
#         user='postgres',
#         password='1234',
#         host='127.0.0.1',
#         port='5432'
#     )
#     cur = conn.cursor()
#     cur.execute('SELECT id, name FROM brands')
#     brands = cur.fetchall()
#     text = ''
#     for i in range(len(brands)):
#         text += str(brands[i][0]) + ' - ' + str(brands[i][1]) + '\n'
#     bot.send_message(message.chat.id, text)
#     cur.close()
#     conn.close()
#
#
# @bot.message_handler(commands=['genres'])
# def getGenres(message):
#     conn = psycopg2.connect(
#         dbname='postgres',
#         user='postgres',
#         password='1234',
#         host='127.0.0.1',
#         port='5432'
#     )
#     cur = conn.cursor()
#     cur.execute('SELECT id, name FROM genres')
#     genres = cur.fetchall()
#     text = ''
#     for i in range(0, len(genres), 1):
#         text += str(genres[i][0]) + ' - ' + genres[i][1] + '\n'
#     bot.send_message(message.chat.id, text)
#     cur.close()
#     conn.close()
#
# @bot.message_handler(commands=['directors'])
# def getDirectors(message):
#     conn = psycopg2.connect(
#         dbname='postgres',
#         user='postgres',
#         password='1234',
#         host='127.0.0.1',
#         port='5432'
#     )
#     cur = conn.cursor()
#     cur.execute('SELECT id, name, surname FROM directors')
#     genres = cur.fetchall()
#     text = ''
#     for i in range(0, len(genres), 1):
#         text += str(genres[i][0]) + ' - ' + genres[i][1]+ ' ' +genres[i][2] + '\n'
#     bot.send_message(message.chat.id, text)
#     cur.close()
#     conn.close()
# @bot.message_handler(commands=['insert_genre'])
# def setGenre(message):
#     bot.send_message(message.chat.id, "Напишите названия жанра для добавления")
#     bot.register_next_step_handler(message, insertGenre)
#     # register_next_step_handler -> Насильственное перенаправление сообщения юзера на указанную функцию
#
#
# def insertGenre(message):
#     conn = psycopg2.connect(
#         dbname='postgres',
#         user='postgres',
#         password='1234',
#         host='127.0.0.1',
#         port='5432'
#     )
#     cur = conn.cursor()
#     genre_name = message.text
#     cur.execute(f"INSERT INTO genres(name) VALUES('{genre_name}')")
#     conn.commit()
#     bot.send_message(message.chat.id, "Genre successfully added!")
#     cur.close()
#     conn.close()
#
# @bot.message_handler(commands=['insert_director'])
# def setDirector(message):
#     bot.send_message(message.chat.id, 'Напишите Имя и Фамилию режесера, через пробел.')
#     bot.register_next_step_handler(message, insertDirector)
# def insertDirector(message):
#     conn = psycopg2.connect(
#         dbname='postgres',
#         user='postgres',
#         password='1234',
#         host='127.0.0.1',
#         port='5432'
#     )
#     cur = conn.cursor()
#     name_surname = message.text
#     cur.execute(f"INSERT INTO directors(name, surname) VALUES('{(name_surname.split())[0]}', '{(name_surname.split())[1]}')")
#     conn.commit()
#     bot.send_message(message.chat.id, "Режесер загружен!")
#     cur.close()
#     conn.close()
#
# @bot.message_handler(commands=['get_film'])
# def get_film_genre(message):
#     conn = psycopg2.connect(
#         dbname='postgres',
#         user='postgres',
#         password='1234',
#         host='127.0.0.1',
#         port='5432'
#     )
#     cur = conn.cursor()
#     cur.execute('SELECT id, name FROM genres')
#     genres = cur.fetchall()
#     text = ''
#     for i in range(0, len(genres), 1):
#         text += str(genres[i][0]) + ' - ' + genres[i][1] + '\n'
#     bot.send_message(message.chat.id, text)
#     cur.close()
#     conn.close()
#     bot.send_message(message.chat.id, 'Напишите ID жанра')
#     bot.register_next_step_handler(message, getIDgenre)
# def getIDgenre(message):
#     conn = psycopg2.connect(
#         dbname='postgres',
#         user='postgres',
#         password='1234',
#         host='127.0.0.1',
#         port='5432'
#     )
#     cur = conn.cursor()
#     cur.execute('SELECT name FROM films WHERE genre_id =' + message.text)
#     genres = cur.fetchall()
#     if len(genres) > 0:
#         text = genres
#         bot.send_message(message.chat.id, text)
#         cur.close()
#         conn.close()
#     else:
#         text = 'Текущего жанра нет в моей колекции фильмов.\nПопробуйте поискать позже)'
#         bot.send_message(message.chat.id, text)
# bot.polling(non_stop=True, interval=0)
# import psycopg2
# from hashlib import sha256
# def setPassword(cur, login):
#     password = input('Придумайте пароль: ')
#     password2 = input("Повторите пароль:")
#     if password != password2:
#         print("Пароли не совпадают! Попробуйте заново!")
#         setPassword(cur, login)
#     else:
#         print('Вы зарегестрированы!')
#     password = sha256(f'{password}'.encode('UTF-8')).hexdigest()
#     cur.execute(f"INSERT INTO users(email, password) VALUES ('{login}', '{password}')")
#     conn.commit()
# def setLogin():
#     login = input()
#     cur = conn.cursor()
#     cur.execute(f"SELECT email FROM users WHERE email='{login}'")
#     emails = cur.fetchall()
#     if len(emails) > 0:
#         print('Этот логин уже занят. Попробуйте другой: ', end='')
#         setLogin()
#     else:
#         setPassword(cur, login)
# def passworing(cur, login):
#     print(login)
#     password = input('Введите пароль: ')
#     password = sha256(f'{password}'.encode('UTF-8')).hexdigest()
#     cur.execute(f"SELECT password FROM users WHERE password='{password}' AND email='{login}'")
#     check = cur.fetchall()
#     if len(check) == 0:
#         print('Не верный пароль! Попробуйте снова.')
#         passworing(cur, login)
#     else:
#         print('Вы успешно вошли в учетную запись!')
# def logining():
#     login = input()
#     cur = conn.cursor()
#     cur.execute(f"SELECT email FROM users WHERE email='{login}'")
#     emails = cur.fetchall()
#     if len(emails) == 0:
#         print('Пользователя с таким логином не существует!\nПопробуйте снова: ', end='')
#         logining()
#     else:
#         passworing(cur, login)
#
# conn = psycopg2.connect(
#     dbname='postgres',
#     user='postgres',
#     password='1234',
#     host='127.0.0.1',
#     port='5432'
# )
# print('Приветствую в поле регестрации!\nНапишите ваш логин: ', end='')
# setLogin()
# print('Пройдите авторизацию. Введите ваш логин:', end='')
# logining()
#
# import psycopg2
#
# conn = psycopg2.connect(
#     dbname='postgres',
#     user='postgres',
#     password='1234',
#     host='127.0.0.1',
#     port='5432'
# )
#
# cur = conn.cursor()
#
# cur.execute(f'SELECT id, name FROM dishes')
# dishes = cur.fetchall()
# for i in range(len(dishes)):
#     print(f'{dishes[i][0]}. {dishes[i][1]}')
#
# dishes_id = input('Введите id блюда: ')
# cur.execute(f'SELECT ingredients.name FROM ingredients JOIN dishes_ingredients ON ingredient_id = ingredients.id JOIN dishes ON dish_id = dishes.id WHERE dish_id = {dishes_id}')
# ing = cur.fetchall()
# for i in range(len(ing)):
#     print(f'{i+1}. {ing[i][0]}')
# cur.close()
# conn.close()

q1 = 'datawgqwgq qwr qwrqw rqw'
q2 = 'dish_2'
if 'dish_' in q1:
    print('YES')
else:
    print('no')