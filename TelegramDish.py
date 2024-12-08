from telebot import TeleBot
import psycopg2
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = TeleBot("7359382385:AAFtKz_2xuunUxI1H-cw95nGbmuCb7TFcK8")
@bot.message_handler(commands=['start'])
def get_info(message):
    bot.send_message(message.chat.id, 'Добро пожаловать!\nВот какие команды у меня есть:\nЧтобы залогиниться или зарегистрироваться напишите команду /login your_number\n(Например:/login 7771234567)\nЧтобы увидеть список БЛЮД /dishes\nЧтобы увидеть список ингредиентов в одном из блюд воспользуйтесь командой /dish_ingredients id_БЛЮДА\n(Например: /dish_ingredients 2)\nЧтобы заказать блюдо /order и выбирите блюдо из предложенных\n')
@bot.message_handler(commands=['dishes'])
def get_dishes(message):
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='1234',
        host='127.0.0.1',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f'SELECT id, name FROM dishes')
    dishes = cur.fetchall()
    text = ''
    for i in range(len(dishes)):
        text += f'{dishes[i][0]}. {dishes[i][1]}\n'
    bot.send_message(message.chat.id, text)
    cur.close()
    conn.close()
@bot.message_handler(commands=['dish_ingredients'])
def dish_ingredients(message):
    dish_id = (message.text).split(' ')[1]
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='1234',
        host='127.0.0.1',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute(f'SELECT ingredients.name FROM ingredients JOIN dishes_ingredients ON ingredient_id = ingredients.id JOIN dishes ON dish_id = dishes.id WHERE dish_id = {dish_id}')
    ing = cur.fetchall()
    text = ''
    for i in range(len(ing)):
        text += f'{i+1}. {ing[i][0]}\n'
    bot.send_message(message.chat.id, text)

    cur.close()
    conn.close()
@bot.message_handler(commands=['order'])
def order(message):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="127.0.0.1",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM dishes")
    keyboard = InlineKeyboardMarkup(row_width=1)
    dishes = cur.fetchall()
    buttons = []
    for dish in dishes:
        buttons.append(InlineKeyboardButton(dish[1], callback_data='dish_' + str(dish[0])))

    for i in range(len(buttons)):
        keyboard.add(buttons[i])

    bot.send_message(message.chat.id, 'Menu:', reply_markup=keyboard)
@bot.callback_query_handler(lambda call: True if 'dish_' in call.data else False)
def dish_callback_handler(call):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="127.0.0.1",
        port="5432"
    )
    cur = conn.cursor()
    dish_id = call.data.split('_')[-1]
    cur.execute(f"SELECT name, price FROM dishes WHERE id={dish_id}")
    dish = cur.fetchone()
    text = f"Вы выбрали {dish[0]} -> {dish[1]} x 1 шт."
    telegram_id = call.from_user.id
    cur.execute(f"SELECT id FROM guests WHERE telegram_id='{telegram_id}' ORDER BY id DESC")
    guest = cur.fetchone()
    if guest is None:
        text = "Нужно залогинится или зарегистрироваться!"
        bot.send_message(call.message.chat.id, text)
        return
    else:
        cur.execute(f"SELECT id FROM orders WHERE status='Creating' AND guest_id = {guest[0]}")
        guest_order = cur.fetchall()
        if len(guest_order) == 0:
            cur.execute(f"INSERT INTO orders(guest_id, total, status) VALUES({guest[0]}, 0, 'Creating') RETURNING id")
            conn.commit()
            guest_order = cur.fetchone()
        order_id = guest_order[0]
        cur.execute(f"SELECT amount FROM dishes_orders WHERE order_id={order_id[0]} AND dish_id={dish_id}")
        ord = cur.fetchall()
        if len(ord) > 0:
            cur.execute(f"UPDATE dishes_orders "
                        f"SET amount=amount + 1, message_id='{call.message.id}' WHERE order_id={order_id[0]} AND dish_id={dish_id}")
            conn.commit()
            text = f"Вы выбрали {dish[0]} -> {dish[1]} x {ord[0][0] + 1} шт."
        else:
            text = f"Вы выбрали {dish[0]} -> {dish[1]} x 1 шт."
            cur.execute(f"INSERT INTO dishes_orders(dish_id, order_id, amount, message_id) "
                        f"VALUES({dish_id}, {order_id[0]}, 1, '{call.message.id}')")
            conn.commit()
    # cur.execute(f"SELECT message_id FROM dishes_orders WHERE order_id={order_id[0]} AND dish_id={dish_id}")
    # message_id = cur.fetchall()[0]
    # bot.delete_message(call.message.chat.id, message_id)

    bot.send_message(call.message.chat.id, text)
    cur.close()
    conn.close()
@bot.message_handler(commands=['login'])
def login(message):
    try:
        phone = (message.text).split()[1]
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='1234',
            host='127.0.0.1',
            port='5432'
        )
        cur = conn.cursor()
        cur.execute(f"SELECT name, surname FROM guests WHERE phone = '{phone}'")
        guest = cur.fetchall()
        if len(guest) > 0:
            bot.send_message(message.chat.id, f'Добро пожаловать {guest[0][0]} {guest[0][1]}!')
        else:
            bot.send_message(message.chat.id, 'Введите своё Имя и Фамилию: ')
            bot.register_next_step_handler(message, reg, cur, conn, phone)
        cur.close()
        conn.close()
    except IndexError:
        bot.send_message(message.chat.id, 'Вы забыли после команды /login ____ <- указать ваш логин.')
def reg(message, cur, conn, phone):
    guest_reg = (message.text).split()
    cur.execute(f"INSERT INTO guests(name, surname, phone, discount, telegram_id) "
                f"VALUES ('{guest_reg[0]}', '{guest_reg[1]}', '{phone}', 50, {message.from_user.id})")
    conn.commit()
    bot.send_message(message.chat.id, 'Вы зарегестрированы!')
    cur.close()
    conn.close()
@bot.message_handler(commands=['history'])
def get_history(message):
    try:
        phone = (message.text).split()[1]
        coonn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='1234',
            host='127.0.0.1',
            port='5432'
        )
        cur = coonn.cursor()
        cur.execute(f"SELECT guests.name, guests.surname, dishes.name, dishes_orders.amount FROM orders"
                     f" JOIN dishes_orders ON orders.id = dishes_orders.order_id"
                     f" JOIN guests ON orders.guest_id = guests.id"
                     f" JOIN dishes ON dishes_orders.dish_id = dishes.id"
                     f" WHERE guests.phone ='{phone}' AND orders.status = 'Creating'")
        history = cur.fetchall()
        if len(history) == 0:
            bot.send_message(message.chat.id, 'Вы еще ничего не заказывали!')
        else:
            text = ''
            for i in range(len(history[0])):
                text += f"{history[i][2]} x {history[i][3]} шт.\n"
            bot.send_message(message.chat.id, f"{history[0][0]} {history[0][1]} выбрал(а):\n{text}")
        cur.close()
        coonn.close()
    except IndexError:
        bot.send_message(message.chat.id, 'Вы забыли после команды /history ____ <- указать ваш логин.')

bot.polling(non_stop=True, interval=0)