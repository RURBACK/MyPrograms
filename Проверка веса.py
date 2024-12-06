import telebot
import datetime 


# Вставьте сюда ваш токен от BotFather
TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Обратная связь с разработчиком\nTelegramm - t.me/RORK_RURBACK")
    bot.send_message(message.chat.id, "Привет! Я бот для расчёта вашего индекса массы тела (ИМТ). Начнём? Отправьте команду /bmi")

@bot.message_handler(commands=['bmi'])
def ask_height(message):
    msg = bot.send_message(message.chat.id, "Введите свой рост в сантиметрах:")
    #print(message.text)
    bot.register_next_step_handler(msg, process_weight)

def process_weight(message):
    try:
        height = float(message.text)
        msg = bot.send_message(message.chat.id, "Отлично! Теперь введите свой вес в килограммах:")
        print(message.text)
        bot.register_next_step_handler(msg, calculate_bmi, height=height)
    except ValueError:
        bot.send_message(message.chat.id, "Рост должен быть числом. Попробуйте ещё раз.")
        return

def calculate_bmi(message, height):
    print(message.text)
    now = datetime.datetime.now()
    x = now.strftime("%H:%M:%S")

    with open('bmi.txt', 'a') as f:
        f.write(f'Сохраненные данные пользователей.\nChat ID: {message.chat.id}, Рост: {height}см, Вес: {message.text}кг, Время записи: {x} \n')
        
    try:
        weight = float(message.text)
        height = height / 100
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            result = f"Ваш индекс массы тела: {bmi:.2f}. Вы в состоянии недовеса."
        elif 18.5 <= bmi < 25:
            result = f"Ваш индекс массы тела: {bmi:.2f}. Вы в нормальном весе."
        elif 25 <= bmi < 30:
            result = f"Ваш индекс массы тела: {bmi:.2f}. Вы в состоянии перевеса."
        elif 30 <= bmi < 35:
            result = f"Ваш индекс массы тела: {bmi:.2f}. Вы в состоянии ожирения."
        elif 35 <= bmi < 40:
            result = f"Ваш индекс массы тела: {bmi:.2f}. Вы в состоянии тяжёлого ожирения."
        else:
            result = f"Ваш индекс массы тела: {bmi:.2f}. Вы в состоянии очень тяжёлого ожирения."

        bot.send_message(message.chat.id, result)
    except ValueError:
        bot.send_message(message.chat.id, "Вес должен быть числом. Попробуйте ещё раз.")
        return

if __name__ == "__main__":
    bot.polling(none_stop=True)
