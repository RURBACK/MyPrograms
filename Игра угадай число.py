import random
from colorama import init, Fore

# Инициализация Colorama
init(autoreset=True)

def main():
    # Приветственное сообщение
    print(Fore.LIGHTBLUE_EX + 'Привет! Я хочу проверить, есть ли у тебя дар предвидения?')
    print(Fore.LIGHTGREEN_EX + 'Давай сыграем в игру угадай число!')

    while True:
        # Запрашиваем ввод числа
        try:
            x = int(input(Fore.LIGHTYELLOW_EX + 'Введите число от 0 до 9: '))
        except ValueError:
            print(Fore.RED + 'Пожалуйста, введите целое число от 0 до 9.')
            continue

        # Проверка диапазона ввода
        if not 0 <= x <= 9:
            print(Fore.RED + 'Число должно быть в диапазоне от 0 до 9.')
            continue

        # Генерация случайного числа
        y = random.randint(0, 9)

        # Сравнение чисел
        if x == y:
            print(Fore.GREEN + f'Поздравляю! Ты угадал! Загаданное мной число было: {y}.')
        else:
            print(Fore.LIGHTMAGENTA_EX + f'К сожалению, ты не угадал. Загаданное мной число: {y}.')
        
        # Предложение сыграть снова
        while True:
            play_again = input(Fore.LIGHTYELLOW_EX + 'Хочешь попробовать ещё раз? (y/n): ').lower()
            if play_again == 'y':
                break
            elif play_again == 'n':
                print(Fore.LIGHTRED_EX + 'Спасибо за игру! До свидания.')
                return
            else:
                print(Fore.RED + 'Неизвестный ответ. Пожалуйста, выберите "y" или "n".')

if __name__ == "__main__":
    main()
