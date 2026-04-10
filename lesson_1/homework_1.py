"""
Задание 1
Работа с переменными, ввод/вывод, функция id()
"""

# 1. Создаём переменные и выводим
name = "Ольга"
age = 25
height = 1.65
print("Имя:", name)
print("Возраст:", age)
print("Рост:", height)

# 2. Запрашиваем данные у пользователя
user_name = input("Введите ваше имя: ")
user_age = input("Введите ваш возраст: ")
user_city = input("Введите ваш город: ")

print("\nВы ввели:")
print("Имя:", user_name)
print("Возраст:", user_age)
print("Город:", user_city)

# 3. Наблюдаем за id()
print("\nНаблюдение за id():")
x = 10
print("x =", x, "id =", id(x))
x = x + 1
print("x =", x, "id =", id(x), "- изменился!")

my_list = [1, 2, 3]
print("Список =", my_list, "id =", id(my_list))
my_list.append(4)
print("Список =", my_list, "id =", id(my_list), "- не изменился!")
