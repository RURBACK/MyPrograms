# Импортируем библиотеки
import random
# Импортируем библиотеку colorama
import colorama
# Для библиотеки colorama 
from colorama import init, Fore, Back, Style
init(autoreset=True) # Инициализация библиотеки colorama

# Создаем пустой словарь для хранения информации о пользователе
task = {}
# Определяем строки для ключей словаря
a = 'Имя: '
b = 'Возраст: '
c = 'Рост: '
# Справка по доступным командам
help_text = """
help: - вывести справку
random: - придумать случайное задание
exit: - выход
task: - ввести информацию о пользователе
show: - вывести информацию о пользователе
add - добавить информацию о пользователе
save: - сохранить информацию о пользователе
load: - загрузить информацию о пользователе
"""
# Словарь с рандомными задачами
tasks = ['Задание: Решить задачу по математике.',
'Задание: Прочитать главу из книги.',
'Задание: Написать эссе на тему "Моя мечта".',
'Задание: Сделать презентацию по истории.',
'Задание: Провести эксперимент по физике.',
'Задание: Почитать книгу.',
'Задание: Посмотреть фильм.',
'Задание: Послушать музыку.',
'Задание: Поиграть в видеоигру.',
'Задание: Посмотреть сериал.',
'Задание: Посмотреть мультфильм.',
'Задание: Посмотреть документальный фильм.',
'Задание: Посмотреть спектакль.',
'Задание: Посмотреть концерт.',
'Задание: Посмотреть выступление в театре.',
'Задание: Посмотреть выступление в цирке.',
'Задание: Посмотреть выступление в музее.',
'Задание: Посмотреть выступление в галерее.',
'Задание: Посмотреть выступление в парке.',
'Задание: Посмотреть выступление в кино,театре или концерте.',
'Задание: Подготовить доклад по биологии.',
'Задание: Составить план на неделю.',
'Задание: Изучить новую программу на компьютере.',
'Задание: Выучить новые слова на иностранном языке.',
'Задание: Нарисовать картину.',
'Задание: Посетить музей или выставку.',
'Задание: Выполнить физические упражнения.',
'Задание: Приготовить новое блюдо.',
'Задание: Почитать статьи по интересующей теме.',
'Задание: Пройти онлайн-курс.',
'Задание: Слушать аудиокнигу.',
'Задание: Убрать комнату.',
'Задание: Позвонить другу и обсудить планы.',
'Задание: Прогуляться в парке.',
'Задание: Помочь кому-то с задачей.']
# Выводим сообщение о вызове справки
print(Fore.YELLOW +"Вызов меню списка команд: help")
# Основной цикл программы
while True:
    # Считываем ввод команды от пользователя
    command = input(Style.BRIGHT +"Введите команду: ").strip().lower()  # Приводим строку к нижнему регистру и убираем лишние пробелы
    # Обработка различных команд
    if command == 'help':  # Команда для вывода справки
        print(Fore.CYAN +f"Меню помощи:\n{help_text}")
    elif command == 'task':  # Команда для ввода информации о пользователе
        date = input(Fore.LIGHTGREEN_EX +"Укажите дату: ") # Вводим дату
        tasks_day = input(Fore.LIGHTGREEN_EX +"Напишите задание на эту дату: ") # Вводим задание
        task['Дата: '] = date # Записываем дату в словарь
        task['Задание: '] = tasks_day # Записываем задание в словарь
        print(Fore.RED +f"Запись создана!: {task}")  # Выводим информацию о пользователе  
    elif command == 'random': # Команда для выбора рандомного задания
        task['Рандомное Задание: '] = random.choice(tasks) # Выбираем рандомное задание
        print(Fore.RED +f"Запись Рандомного задания создана!: {task}") # Выводим информацию о пользователе
    elif command == 'add': # Команда для добавления нового задания
        name = input(Fore.LIGHTGREEN_EX +"Введите имя: ") # Вводим имя
        age = input(Fore.LIGHTGREEN_EX +"Введите возраст: ") # Вводим возраст
        height = input(Fore.LIGHTGREEN_EX +"Введите рост: ") # Вводим рост
        task[a] = name # Записываем имя в словарь
        task[b] = age # Записываем возраст в словарь
        task[c] = height # Записываем рост в словарь
        print(Fore.RED +f"Запись создана!: {task}") 
    elif command == 'exit':  # Команда для выхода из программы
        print(Fore.RED +"Выход из программы.") # Выводим сообщение о выходе
        break # Выходим из цикла
    elif command == 'show':  # Команда для отображения введенной информации
        for key, value in task.items(): # Выводим все пары ключ-значение
            print(f"{key}: {value}") # Выводим все пары ключ-значение
    elif command == 'save':  # Команда для сохранения информации в файл
        try: # Обработка ошибок при сохранении
            with open('task.txt', 'w', encoding='utf-8') as file: # Создаем файл
                for key, value in task.items(): # Выводим все пары ключ-значение в файл
                    file.write(f"{key}: {value}\n")  # Сохраняем каждую пару ключ-значение в отдельной строке
            print(Back.GREEN +"Информация успешно сохранена!") # Выводим сообщение о сохранении
        except IOError as e: # Обработка ошибок при сохранении 
            print(Fore.RED +f"Произошла ошибка при сохранении файла: {e}") # Выводим сообщение о сохранении файла
    elif command == 'load':  # Команда для загрузки информации из файла
        try: # Обработка ошибок при загрузке данных
            with open('task.txt', 'r', encoding='utf-8') as file: # Создаем файл 
                task.clear()  # Очищаем текущий словарь перед загрузкой новых данных
                for line in file: # Перебираем все строки в файле
                    key, value = line.strip().split(': ', maxsplit=1)  # Разделяем строку на ключ и значение
                    task[key.strip()] = value.strip()  # Добавляем данные в словарь
            print(Fore.RED +"Информация успешно загружена!") # Выводим сообщение о загрузке данных
        except FileNotFoundError: # Обработка ошибок при загрузке данных
            print(Fore.RED +"Файл не найден! Попробуйте сначала сохранить данные.") # Выводим сообщение об ошибке при загрузке данных
        except IOError as e: # Обработка ошибок при загрузке данных
            print(Fore.RED +f"Произошла ошибка при чтении файла: {e}") # Выводим сообщение об ошибке при загрузке данных
    else:  # Если введена неизвестная команда
        print(Fore.RED +"Неизвестная команда. Повторите попытку.") # Выводим сообщение о неизвестной команда