"""
Домашнее задание 3
Математические функции и генерация шапки процессуального документа
"""

# Импортируем данные судов из соседнего файла
from lesson_2_data import courts

# ========== 1. МАТЕМАТИЧЕСКИЕ ФУНКЦИИ ==========

def factorial(n):
    """Возвращает факториал числа n"""
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

def max_of_three(numbers):
    """Возвращает наибольшее число из трёх"""
    return max(numbers)

def right_triangle_area(a, b):
    """Возвращает площадь прямоугольного треугольника"""
    return 0.5 * a * b

# ========== 2. ФУНКЦИЯ ОПРЕДЕЛЕНИЯ СУДА ПО НОМЕРУ ДЕЛА ==========

def get_court(case_number):
    """По номеру дела возвращает название и адрес суда"""
    court_code = case_number[:3]
    court_info = courts.get(court_code)
    if court_info:
        return court_info["court_name"], court_info["court_address"]
    return "Суд не найден", "Адрес не известен"

# ========== 3. ФУНКЦИЯ ГЕНЕРАЦИИ ШАПКИ ==========

def generate_header(respondent, case_number):
    """Генерирует шапку процессуального документа"""
    
    # Данные истца (твои)
    plaintiff = {
        "name": "Гусакова Ольга Ивановна",
        "inn": "123456789012",
        "ogrnip": "123456789012345",
        "address": "г. Москва, ул. Своя, д. 1"
    }
    
    # Получаем суд по номеру дела
    court_name, court_address = get_court(case_number)
    
    # Формируем шапку с помощью f-string
    header = f"""
В {court_name}
Адрес: {court_address}

Истец: {plaintiff['name']}
ИНН {plaintiff['inn']}
ОГРНИП {plaintiff['ogrnip']}
Адрес: {plaintiff['address']}

Ответчик: {respondent.get('name', 'Не указано')}
ИНН {respondent.get('inn', 'Не указан')}
ОГРН {respondent.get('ogrn', 'Не указан')}
Адрес: {respondent.get('address', 'Не указан')}

Номер дела: {case_number}
"""
    return header.strip()

# ========== 4. ФУНКЦИЯ ДЛЯ МАССОВОЙ ГЕНЕРАЦИИ (ЦИКЛ FOR) ==========

def print_all_headers(respondents_list, case_number):
    """Для каждого ответчика печатает шапку"""
    for i, respondent in enumerate(respondents_list, 1):
        print("\n" + "=" * 50)
        print(f"Ответчик №{i}")
        print("=" * 50)
        print(generate_header(respondent, case_number))

# ========== 5. ПРОВЕРКА РАБОТЫ ==========

if __name__ == "__main__":
    print("=== Математические функции ===")
    print(f"Факториал 5: {factorial(5)}")
    print(f"Максимум из (10, 25, 7): {max_of_three((10, 25, 7))}")
    print(f"Площадь треугольника 3 и 4: {right_triangle_area(3, 4)}")
    
    print("\n=== Генерация шапки ===")
    
    # Тестовые данные ответчиков
    test_respondents = [
        {
            "name": "ООО \"Ромашка\"",
            "inn": "1234567890",
            "ogrn": "123456789012345",
            "address": "г. Москва, ул. Цветочная, д. 5"
        }
    ]
    
    print_all_headers(test_respondents, "А40-123456/2023")
