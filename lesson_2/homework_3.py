"""
Домашнее задание 3
Математические функции и генерация шапки процессуального документа
"""

# Импортируем данные из файла
from lesson_2_data import courts, respondents

# ========== 1. МАТЕМАТИЧЕСКИЕ ФУНКЦИИ ==========

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def max_of_three(numbers):
    return max(numbers)

def right_triangle_area(a, b):
    return 0.5 * a * b

# ========== 2. ОПРЕДЕЛЕНИЕ СУДА ПО НОМЕРУ ДЕЛА ==========

def get_court(case_number):
    court_code = case_number[:3]
    court_info = courts.get(court_code)
    if court_info:
        return court_info["court_name"], court_info["court_address"]
    return "Суд не найден", "Адрес не известен"

# ========== 3. ГЕНЕРАЦИЯ ШАПКИ ==========

def generate_header(respondent, case_number):
    plaintiff = {
        "name": "Гусякова Ольга Ивановна",
        "inn": "123456789012",
        "ogrnip": "123456789012345",
        "address": "г. Москва, ул. Своя, д. 1"
    }
    
    court_name, court_address = get_court(case_number)
    
    header = f"""
В {court_name}
Адрес: {court_address}

Истец: {plaintiff['name']}
ИНН {plaintiff['inn']}
ОГРНИП {plaintiff['ogrnip']}
Адрес: {plaintiff['address']}

Ответчик: {respondent.get('full_name', respondent.get('name', 'Не указано'))}
ИНН {respondent.get('inn', 'Не указан')}
ОГРН {respondent.get('ogrn', 'Не указан')}
Адрес: {respondent.get('address', 'Не указан')}

Номер дела: {case_number}
"""
    return header.strip()

# ========== 4. ФУНКЦИЯ ДЛЯ МАССОВОЙ ГЕНЕРАЦИИ ==========

def print_all_headers(respondents_list, case_number):
    for i, resp in enumerate(respondents_list, 1):
        print("\n" + "=" * 60)
        print(f"Ответчик №{i}")
        print("=" * 60)
        print(generate_header(resp, case_number))

# ========== 5. ПРОВЕРКА РАБОТЫ ==========

if __name__ == "__main__":
    print("=" * 50)
    print("МАТЕМАТИЧЕСКИЕ ФУНКЦИИ")
    print("=" * 50)
    print(f"Факториал 5: {factorial(5)}")
    print(f"Максимум из (10, 25, 7): {max_of_three((10, 25, 7))}")
    print(f"Площадь треугольника 3 и 4: {right_triangle_area(3, 4)}")
    
    print("\n" + "=" * 50)
    print("ГЕНЕРАЦИЯ ШАПОК ДЛЯ ОТВЕТЧИКОВ")
    print("=" * 50)
    
    # Используем реальных ответчиков из файла (первые 5)
    print_all_headers(respondents[:5], "А40-123456/2023")
