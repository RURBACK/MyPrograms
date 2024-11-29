import time
import datetime
from colorama import init, Fore, Back, Style
import webbrowser
init(autoreset=True)
print(Fore.LIGHTWHITE_EX +Style.BRIGHT +"Автор программы: Moriarty in the Rabochka poselok")

while True:
            password = input(Fore.LIGHTGREEN_EX +"Введите пароль: ")
            if password == "1":
                print(Fore.LIGHTGREEN_EX +"Пароль верный")
                break
            else:
                print(Fore.RED +"Пароль неверный")
                False

class Pet:
    def __init__(self):
        self.name = None
        self.age = None
        self.color = None
        self.tasks = {}
        self.time = None

    def calories_calc_dogy(self):
        try:
            masa = int(input("Введите вес вашей собаки: "))
            adult = int(masa) * 110
            young = int(masa) * 200
            print(Fore.GREEN +f"Ваша [взрослая] собака должна потреблять в сутки {adult} Килло\Каллорий")
            print(Fore.GREEN +f"Ваша [растущая] собака должна потреблять в сутки {young} Килло\Каллорий")
        except ValueError:
            print(Fore.RED +"Ошибка ввода")              
                
    def calories_calc_kity(self):
        try:
            masa = int(input("Введите вес вашей кошки: "))
            adult = int(masa) * 130
            young = int(masa) * 210
            print(Fore.GREEN +f"Ваша [взрослая] кошка должна потреблять в сутки {adult} Килло\Каллорий")
            print(Fore.GREEN +f"Ваша [растущая] кошка должна потреблять в сутки {young} Килло\Каллорий")
        except ValueError:
            print(Fore.RED +"Ошибка ввода")

    def clear_file(self):
        try:
            with open('Список_животных.txt', 'w'):
                print("Файл очищен!")
        except FileNotFoundError:
            print(Fore.RED +"Ошибка ввода")
        except Exception as e:
            print(Fore.RED +f"Ошибка чтения файла {e}")

    def calcul_ator(self):
        print(Fore.GREEN +"Калькулятор активирован.")
        print(Fore.YELLOW +"Введите арифметическую операцию\nПример: 2+2\nИ нажмите ENTER ")
        while True:
            value = input(": ")
            print(Fore.GREEN +"Вы ввели:",'|'.join(value))
            if value == 'exit':
                print(Fore.RED +"Вы вышли из калькулятора")
                break
            for i in value:
                if i == "+":
                    value = value.split("+")
                    res = int(value[0]) + int(value[1])
                    print("Ответ:",res) 
                elif i == "-":
                    value = value.split("-")
                    res = int(value[0]) - int(value[1])
                    print("Ответ:",res)
                elif i == "*":
                    value = value.split("*")
                    res = int(value[0]) * int(value[1])
                    print("Ответ:",res)
                elif i == "/":
                    value = value.split("/")
                    res = int(value[0]) / int(value[1])
                    print("Ответ:",res)
                  
    HELP = """
    1. _К_о_ш_к_и_
    2. _С_о_б_а_к_и_
    3. Ваши заметки и назначения
    4. Загрузить ранее внесенные данные
    5. Помошник Чумба
    6. Жми если нужно что-то посчитать
    7. Очистить все сохраненные данные
    8. Калькулятор калорий для собаки
    9. Калькулятор калорий для кошки
    10. Завершение работы
    """

    def cheburek_gek(self):
        print(Fore.LIGHTGREEN_EX +"Вы вызываете помошника чумбу!\n")
        print(Fore.LIGHTGREEN_EX +"Вот что я могу рассказать\n")
        time.sleep(2)
        url = 'https://ru.wikipedia.org/wiki/Млекопитающие'
        webbrowser.open(url)

    def set_time(self):
        self.time = datetime.datetime.now()
        return self.time

    def set_pet_info(self):
        task = {}
        self.name = input(Fore.LIGHTGREEN_EX +"Введите кличку питомца: ")
        self.age = input(Fore.LIGHTGREEN_EX +"Введите возраст питомца: ")
        self.color = input(Fore.LIGHTGREEN_EX +"Введите цвет питомца: ")
        task['Кличка ' + self.name] = 'Возраст ' + self.age,'Цвет ' + self.color
        print("Обрабатываю данные")
        print(task)
        time.sleep(2)
        comans = input("Желаете сохранить данные? Да\Нет: ").lower()
        if comans == "да":
            pet = Pet()
            with open("Список_животных.txt", "w") as file:
                time_to_write = pet.set_time()
                file.write(f"Дата записи: {time_to_write}\n")
                file.write(f"Исследуемый обьект: {task}\n")
                print(task)
        elif comans == "нет":
            print("Данные не сохранены")
        else:
            print("Неверный ввод")
            
    def show_pet_info(self):
        print(f"Кличка: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Цвет: {self.color}")

    def manage_tasks(self):
        while True:
            command = input(Fore.LIGHTBLUE_EX +"Приступить к записи команда: add\n: ").lower()
            if command == "add":
                try:
                    date = input(Fore.LIGHTGREEN_EX +"Введите дату задачи: ")
                    task = input(Fore.LIGHTGREEN_EX +"Введите задачу: ")
                    self.tasks[date] = task
                    print(f"Добавлена задача '{task}' на {date}")
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
            elif command == "show":
                for date, task in self.tasks.items():
                    print(f"{date}: {task}")
            elif command == "save":
                try:
                    with open("Задачи_на_даты.txt", "a") as file:
                        for date, task in self.tasks.items():
                            file.write(f"{date}: {task}\n")
                    print(f"Сохранено в файл {file.name}")
                except Exception as e:
                    print(Fore.RED +f"Произошла ошибка при сохранении файла: {e}")
            elif command == "load":
                try:
                    with open("Задачи_на_даты.txt", "r") as file:
                        content = file.read()
                        print(content)
                except FileNotFoundError:
                    print("Файл не найден.")
                except Exception as e:
                    print(Fore.RED +f"Произошла ошибка при чтении файла: {e}")
            elif command == "exit":
                return
            else:
                print(Fore.RED +"Команда не найдена")

def main():
    print("")
    pet = Pet()
    pet.set_time()
    print(Fore.LIGHTGREEN_EX +f"Выберите действие:")
    print(Fore.WHITE +f"1. _К_о_ш_к_и_")
    print(Fore.LIGHTGREEN_EX +f"2. _С_о_б_а_к_и_")
    print(Fore.LIGHTMAGENTA_EX +f"3. Ваши заметки и назначения")
    print(Fore.LIGHTBLACK_EX +f"4. Загрузить ранее внесенные данные")
    print(Fore.LIGHTCYAN_EX +f"5. Помошник Чумба")
    print(Fore.LIGHTYELLOW_EX +f"6. Жми если нужно что-то посчитать")
    print(Fore.LIGHTRED_EX +f"7. Очистить все сохраненные данные")
    print(Fore.GREEN +"8. Калькулятор калорий для собаки")
    print(Fore.LIGHTBLUE_EX +f"9. Калькулятор калорий для кошки")
    print(Fore.LIGHTRED_EX +f"10. Завершение работы")
    while True:
        print("11. Помощ по командам")
        try:
            choice = int(input(Fore.YELLOW +"Ваш выбор: "))
        except ValueError:
            print(Fore.RED +"Некорректный ввод. Попробуйте еще раз.")
            continue

        if choice == 1 or choice == 2:
            pet = Pet()
            pet.set_pet_info()
            pet.show_pet_info()
        elif choice == 3:
            pet = Pet()
            pet.manage_tasks()
        elif choice == 4:
            try:
                with open("Список_животных.txt", "r") as file:
                    countent = file.read()
                    print(countent)
            except FileNotFoundError:
                print("Файл не найден.")
            except Exception as e:
                print(Fore.RED +f"Произошла ошибка при чтении файла: {e}")
                
        elif choice == 5:
            pet = Pet()
            pet.cheburek_gek() 
        elif choice == 6:
            pet = Pet()
            pet.calcul_ator()
        elif choice == 7:
            pet = Pet()
            pet. clear_file()
        elif choice == 8:
            pet = Pet()
            pet.calories_calc_dogy()
        elif choice == 9:
            pet = Pet()
            pet.calories_calc_kity()
        elif choice == 10:
            print(Fore.RED +"Завершение работы...")
            break
        elif choice == 11:
            pet = Pet() 
            print(pet.HELP)
        else:
            print(Fore.RED +"Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()