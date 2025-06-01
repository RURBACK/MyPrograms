print("Привет Серега Мальцев\nЯ написал эту программу для тебя!")
print("Автор Витя Фишер")
while True:
    try:
        old_age = int(input("Введите возраст отца: "))
        yong_man = int(input("Введите возраст сына: "))
        if yong_man > old_age:
            print("Сын не может быть старше отца!")
            continue
        mat = old_age - yong_man
        mat2 = old_age - 2 * yong_man
        if mat2 < 0:
            print(f"Разница {mat}, Будет вдвое старше сына прибавив {abs(mat2)} лет.")
        else:
            print(f"Разница {mat}, Будет вдвое старше сына убавив {mat2} лет.")
        a = input("Хотите продолжить? Да/Нет :_").lower()
        if a == "да":
            continue
        elif a == "нет":
            break
        else:
            print("Не понимаю вас. Начнем сначала.")
            continue
    except ValueError:
        print("Ошибка! Введенный знак не Является целым числом!")
        continue
