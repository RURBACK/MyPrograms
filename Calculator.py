import re

def calculate(expression): # Расчет выражения
    pattern = r'(\d+)\s*([-+*/])\s*(\d+)' # Регулярное выражение для вычисления
    match = re.match(pattern, expression) # Поиск совпадений
    
    if not match: # Если совпадений не найдено
        return "Некорректное выражение." # Возвращаем ошибку
    
    num1, op, num2 = match.groups() # Получение значений 
    num1 = float(num1) # Преобразование в число
    num2 = float(num2) # Преобразование в число
    
    if op == '+': # Если операция равна +
        result = num1 + num2 # Вычисление

    elif op == '-': # Если операция равна -
        result = num1 - num2 # Вычисление 
        
    elif op == '*': # Если операция равна *
    
        result = num1 * num2 # Вычисление
    elif op == '/': # Если операция равна /
    
        if num2 == 0: # Если деление на ноль
            return "Деление на ноль!" # Возвращаем ошибку 
        result = num1 / num2 # Вычисление
    
    return f"Ваш ответ равен: {result:.2f}" # Возвращаем ответ

if __name__ == "__main__": # Инициализация программы
    while True: # Пока не будет выхода из программы
        user_input = input("Ввод: ") # Ввод пользователем
        
        if user_input.lower() == "exit": # Если пользователь ввел exit
            print("Выход из программы.") # Выводим сообщение
            break # Выходим из программы

        answer = calculate(user_input) # Вычисляем ответ
        print(answer) # Выводим ответ