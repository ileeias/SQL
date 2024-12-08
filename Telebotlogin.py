import psycopg2
from hashlib import sha256
import telebot.types
from telebot import TeleBot

bot = TeleBot("7375162409:AAHYUQGq45SR8VdeokV--IiX272UrzBO8t4")

@bot.message_handler(content_types=['text'])
def hello(message):
    global conn
    if message.text == 'Привет':
        keyboard = telebot.types.InlineKeyboardMarkup()
        log = telebot.types.InlineKeyboardButton(text='Авторизоваться', callback_data='login')
        reg = telebot.types.InlineKeyboardButton(text='Зарегестрироваться', callback_data='register')
        keyboard.row(log, reg)
        bot.send_message(message.chat.id, 'Добро пожаловать! У вас есть учетная запись?', reply_markup=keyboard)
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='1234',
            host='127.0.0.1',
            port='5432'
        )
    else:
        bot.send_message(message.chat.id, 'Напиши слово "Привет"')
@bot.callback_query_handler(lambda x: True)
def keyboard_worker(callback):
    if callback.data == 'login':
        bot.send_message(callback.message.chat.id, 'Введите ваш логин для авторизации:')
        bot.register_next_step_handler(callback.message, logining)
        # logining(callback.message)
    elif callback.data == 'register':
        bot.send_message(callback.message.chat.id, 'Введите ваш логин для регистрации:')
        bot.register_next_step_handler(callback.message, setLogin)
def setPassword(message, cur, login):
    password = message.text
    bot.send_message(message.chat.id, 'Повторите пароль:')
    bot.register_next_step_handler(message, setPassword2, cur, login, password)
def setPassword2(message, cur, login, password):
    password2 = message.text
    if password != password2:
        bot.send_message(message.chat.id, 'Пароли не совпадают! Попробуйте заново!')
        bot.send_message(message.chat.id, 'Придумайте пароль:')
        bot.register_next_step_handler(message, setPassword, cur, login)
    else:
        bot.send_message(message.chat.id, 'Вы зарегестрированы!')
        password = sha256(f'{password}'.encode('UTF-8')).hexdigest()
        cur.execute(f"INSERT INTO users(email, password) VALUES ('{login}', '{password}')")
        conn.commit()
        cur.close()
        conn.close()
def setLogin(message):
    login = message.text
    cur = conn.cursor()
    cur.execute(f"SELECT email FROM users WHERE email='{login}'")
    emails = cur.fetchall()
    if len(emails) > 0:
        bot.send_message(message.chat.id, 'Этот логин уже занят. Попробуйте другой:')
        bot.register_next_step_handler(message, setLogin)
    else:
        bot.send_message(message.chat.id, 'Придумайте пароль:')
        bot.register_next_step_handler(message, setPassword, cur, login)
def passworing(message, login, cur):
    password = message.text
    password = sha256(f'{password}'.encode('UTF-8')).hexdigest()
    cur.execute(f"SELECT password FROM users WHERE password='{password}' AND email='{login}'")
    check = cur.fetchall()
    if len(check) == 0:
        bot.send_message(message.chat.id, 'Не верный пароль! Попробуйте снова.')
        bot.register_next_step_handler(message, passworing, login, cur)
    else:
        bot.send_message(message.chat.id, 'Вы успешно вошли в учетную запись!')
        cur.close()
        conn.close()
def logining(message):
    login = message.text
    cur = conn.cursor()
    cur.execute(f"SELECT email FROM users WHERE email='{login}'")
    emails = cur.fetchall()
    if len(emails) == 0:
        bot.send_message(message.chat.id, 'Пользователя с таким логином не существует!\nПопробуйте снова:')
        bot.register_next_step_handler(message, logining)
    else:
        bot.send_message(message.chat.id, 'Введите ваш пароль:')
        bot.register_next_step_handler(message, passworing, login, cur)

def register(message):
    bot.send_message(message.chat.id, 'Введите ваш логин для регистрации:')

bot.polling(non_stop=True, interval=0)
