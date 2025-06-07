import random
from colorama import Fore, Back, Style, init
import time
init(autoreset=True)

print(Fore.GREEN+"Рабочий поселок продакшн.\nВиладж интертеймант.\nВитя Фишер представляет вашему взору...")
print(Fore.YELLOW+"ПОПРОБУЙ НАЕБАТЬ V: 0.1")

HELP = """
ПРАВИЛА ТАКОВЫ
Вы должны попытаться угадать какое число загадала моя программа.
Введите предполагаемое вами число от 1 до 10 и нажмите ENTER
"""

print(HELP)

def ran(x):
    y = random.randint(1, 10)
    if x != y:
        print(Fore.RED+f"Вы не угадали! Я загадывал число {y}")
    else:
        print(Fore.LIGHTGREEN_EX+f"Все верно! Я загадал тоже цифру {y}")

while True:
    try:
        x = int(input(Fore.LIGHTGREEN_EX+"Введите число: "))
        if x <= 0:
            print(Fore.LIGHTBLUE_EX+"Вводите цифры не ниже 1")
            continue
        elif x > 10:
            print(Fore.LIGHTBLUE_EX+"Не больше 10!")
            continue 
        ran(x)
        while True:
            z = input(Fore.LIGHTYELLOW_EX+"Продолжить? y/n : ")
            if z == "n":
                print(Fore.LIGHTMAGENTA_EX+"Программа завершена!")
                time.sleep(1)
                exit()
            elif z == "y":
                break
            else:
                print(Fore.RED+"Только латинские буквы!")
                continue
    except ValueError:
        print(Fore.LIGHTBLUE_EX+"Вводите только числа!")
        continue