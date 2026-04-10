"""
Задание 2 и 3
Перевод секунд и сумма n + nn + nnn
"""

# Задание 2
print("=== Задание 2 ===")
seconds = input("Введите время в секундах: ")

if seconds.isdigit():
    total_seconds = int(seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    
    print("Часы:", hours)
    print("Минуты:", minutes)
    print("Секунды:", secs)
else:
    print("Ошибка: нужно ввести целое число!")

# Задание 3
print("\n=== Задание 3 ===")
n = input("Введите число от 1 до 9: ")

if n.isdigit():
    n_int = int(n)
    if 1 <= n_int <= 9:
        nn = int(n * 2)
        nnn = int(n * 3)
        result = n_int + nn + nnn
        print(f"{n_int} + {nn} + {nnn} = {result}")
    else:
        print("Ошибка: число должно быть от 1 до 9!")
else:
    print("Ошибка: введите одну цифру!")
