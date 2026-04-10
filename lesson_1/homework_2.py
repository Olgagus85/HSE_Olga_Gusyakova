print("Задание 2")
sec = input("Введи секунды: ")
if sec.isdigit():
    s = int(sec)
    print("Часы:", s // 3600)
    print("Минуты:", (s % 3600) // 60)
    print("Секунды:", s % 60)
else:
    print("Ошибка")
