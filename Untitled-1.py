import random

task = {}

HELP = '''
help - помощ по командам.
save - сохранить.
load - загрузить.
random_task - Придумать вымышленную личность.
add - Внести новуцю запись о человеке.
calk - вычислить зарплату.
'''

def random_task():
    global task
    task['Имя: '] = random.choice(['Иван', 'Петр', 'Сергей', 'Дмитрий', 'Александр'])
    task['Возраст: '] = random.randint(1, 100)
    task['Вес: '] = random.randint(40, 200)
    task['Рост: '] = random.randint(100, 200)
    task['Пол: '] = random.choice(['Мужской', 'Женский'])
    task['Цвет глаз: '] = random.choice(['Зеленый', 'Синий', 'Красный', 'Желтый'])
    task['Цвет волос: '] = random.choice(['Черный', 'Рыжий', 'Блондин', 'Русый'])
    task['Цвет кожи: '] = random.choice(['Белый', 'Черный', 'Коричневый', 'Желтый'])
    task['Цвет волос: '] = random.choice(['Черный', 'Рыжий', 'Блондин', 'Русый'])
    return print(task)
    
def main():
    global task
    print('Добро пожаловать в программу "Записная книжка"\nДля начала работы введите команду add\nДля выхода введите exit')
    while True:
        comand = input('Введите команду: ')
        if comand == 'add':
            name = input("Введите имя: ").title()
            age = input("Введите возраст: ")
            weith= input("Введите вес: ")
            task['Имя: '] = name 
            task['Возраст: '] = age + ' лет'
            task['Вес: '] = weith + ' кг'
            print(task)
        elif comand == 'exit':
            break
        else:
            print('Такой команды нет!')     
            
def save():
        global task
        with open('task.txt', 'w') as file:
            file.write(str(task))
        print('Данные сохранены')
        
def load():
    global task
    with open('task.txt', 'r') as file:
        task = eval(file.read())
    print("Данные загружены!")
    print(task)

def menu():
    global task
    print("Введите help для помощи по командам.\n")
    while True:  
        tasks = input('Выберите действие: ')
        if tasks == 'help':
            print(HELP)
        elif tasks == 'save':
            save()
        elif tasks == 'load':
            load()
        elif tasks == 'exit':
            break
        elif tasks == 'add':
            main()
        elif tasks == 'random':
            random_task()
        elif tasks == 'calk':
            calculator()
        else:
            print('Такой команды нет!')

def calculator():
    comand = input('Введите add для вызова калькулятора или exit для выхода: ')
    if comand == 'add':
        while True:    
            try:
                a = int(input('Введите число: '))
                b = int(input('Введите число: '))
            except ValueError:
                print('Введите число!')
                y = input('Оператор вычисления +, -, *, /, **,: ')
                if y == '+':
                    print(a + b)
                elif y == '-':
                    print(a - b)
                elif y == '*':
                    print(a * b)
                elif y == '/':
                    print(a / b)
                elif y == '**':
                    x = int(input('Введите число и я возведу его во вторую степень: '))
                    q = x ** 2
                    print('Ответ = ' + str(q) + 'в квадрате')
                    break
                elif y == 'exit':
                    break
                else:
                    print('Такого оператора нет!')
                    continue
    else:
        print('Такой команды нет!')
            
        

if __name__ == '__main__':
    menu()