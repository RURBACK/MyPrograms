import telebot
import re
from telebot import types

def calculate(message):
    x = message.text.strip()

    patern = r'(\d+)\s*([*/+-])\s*(\d+)'
    match = re.match(patern, x)

    if not match:
        return bot.reply_to(message, "Некорректное выражение.")
    num1, op, num2 = match.groups()
    num1 = float(num1)
    num2 = float(num2)
    
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            return bot.reply_to(message, "Деление на ноль!")   
        result = num1 / num2
    print(f"Пользователь {message.from_user.username} ввел: {x} На что получил ответ: {result:.6g}\n")
    return bot.reply_to(message,f"Ваш ответ равен: {result:.6g}\nОперация завершенна!",reply_markup=keyboard)
    
        

def square(message):
    try:
        number = float(message.text)
        square_result = number ** 2
        print(f"Пользователь {message.from_user.username} ввел: {number} На что получил ответ: {square_result:.6g}\n")
        bot.reply_to(message, f"Квадрат числа {number} равен {square_result:.6g}.\nОперация завершена!",reply_markup=keyboard)
        
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите корректное число.")

def cube(message):
    try:
        number = float(message.text)
        cube_result = number ** 3
        print(f"Пользователь {message.from_user.username} ввел: {number} На что получил ответ: {cube_result:.6g}\n")
        bot.reply_to(message, f"Куб числа {number} равен {cube_result:.6g}.\nОперация завершена!",reply_markup=keyboard)
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите корректное число.")
    

token = '8039833591:AAEomAmZX4tkxtxoWDmfezrl77r8hnJmF-g' #token

bot = telebot.TeleBot(token)
print("Бот запущен...")

IMAGE_PATH = r'D:\Projekt\Trening\image.jpg'

keyboard = types.ReplyKeyboardMarkup(row_width=3)
button1 = types.KeyboardButton('Квадрат')
button2 = types.KeyboardButton('Куб')
button3 = types.KeyboardButton('Калькулятор')
keyboard.add(button1, button2, button3)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет я бот математик.')
    with open(IMAGE_PATH, 'rb') as photo:
        # Отправляем изображение
        bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id,'Выберите действие:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    x = message.text.strip()
    if x == 'Квадрат':
        msg = bot.send_message(message.chat.id, "Введите число")
        bot.register_next_step_handler(msg, square)
    elif x == 'Куб':
        msg = bot.send_message(message.chat.id, "Введите число")
        bot.register_next_step_handler(msg, cube)
    elif x == 'Калькулятор':   
        msg = bot.send_message(message.chat.id, "Введите выражение")
        bot.register_next_step_handler(msg, calculate)
    

bot.infinity_polling()
