import sys
from colorama import init, Fore
init(autoreset=True)
print(Fore.LIGHTCYAN_EX +"Контакты автора: https://t.me/RORK_RURBACK")
def calculate_bmi():
    try:
        height = float(input(Fore.LIGHTGREEN_EX +"Введите свой рост в сантиметрах: "))
        weight = float(input(Fore.LIGHTGREEN_EX +"Введите свой вес в килограммах: "))
        height = height / 100
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            print(Fore.LIGHTYELLOW_EX +f"Ваш индекс массы тела: {bmi:.2f}. Вы в состоянии недовеса.")
        elif 18.5 <= bmi < 25:
            print(Fore.LIGHTGREEN_EX +f"Ваш индекс массы тела: {bmi:.2f}. Вы в нормальном весе.")
        elif 25 <= bmi < 30:
            print(Fore.LIGHTYELLOW_EX +f"Ваш индекс массы тела: {bmi:.2f}. Вы в состоянии перевеса.")
        elif 30 <= bmi < 35:
            print(Fore.LIGHTRED_EX +f"Ваш индекс массы тела: {bmi:.2f}. Вы в состоянии ожирения 1й стадии.")
        elif 35 <= bmi < 40:
            print(Fore.LIGHTRED_EX +f"Ваш индекс массы тела: {bmi:.2f}. Вы в состоянии тяжелого ожирения 2й стадии.")
        else:
            print(Fore.LIGHTRED_EX +f"Ваш индекс массы тела: {bmi:.2f}. Вы в состоянии очень тяжелого ожирения 3й стадии.")
    
    except ValueError:
        print(Fore.LIGHTRED_EX +"Пожалуйста, введите корректные числовые данные.")
while True:
    calculate_bmi()
    x = input(Fore.LIGHTRED_EX +"Для выхода или продолжения выберите y/n.").lower()
    if x == "y": 
        continue
    elif x == "n":
        print(Fore.LIGHTRED_EX +"До свидания!")
        sys.exit(1)
    else:
        print(Fore.LIGHTRED_EX +"Пожалуйста, введите корректные данные.")
