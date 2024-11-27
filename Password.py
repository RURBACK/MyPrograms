import secrets
import string
while True:
    try:
        number_of_characters = int(input("Укажи количество символов в пароле: "))
    except ValueError:
        print("Введите число!")
    if number_of_characters < 1:
            print("Введите число больше 0!")
    else:
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(number_of_characters)) 
        print("Пароль сгенерирован: ",password) 