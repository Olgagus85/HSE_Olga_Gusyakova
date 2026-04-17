"""
Домашнее задание 4 (дополнительное)
Функция для валидации ИНН (10 или 12 цифр)
"""

def validate_inn(inn_str: str) -> bool:
    """
    Основная функция для проверки корректности ИНН.
    Возвращает True, если ИНН валидный, иначе False.
    """
    inn_str = inn_str.strip()
    
    if not inn_str.isdigit():
        return False
    
    if len(inn_str) == 10:
        return validate_inn_legal_entity(inn_str)
    elif len(inn_str) == 12:
        return validate_inn_individual(inn_str)
    else:
        return False


def validate_inn_legal_entity(inn: str) -> bool:
    """
    Проверяет ИНН для юридического лица (10 цифр).
    """
    coefficients = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    
    control_sum = 0
    for i in range(9):
        control_sum += int(inn[i]) * coefficients[i]
    
    check_digit = control_sum % 11
    if check_digit > 9:
        check_digit %= 10
    
    return check_digit == int(inn[9])


def validate_inn_individual(inn: str) -> bool:
    """
    Проверяет ИНН для физического лица или ИП (12 цифр).
    """
    coefficients_first = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    
    control_sum_1 = 0
    for i in range(10):
        control_sum_1 += int(inn[i]) * coefficients_first[i]
    
    check_digit_1 = control_sum_1 % 11
    if check_digit_1 > 9:
        check_digit_1 %= 10
    
    if check_digit_1 != int(inn[10]):
        return False
    
    coefficients_second = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    
    control_sum_2 = 0
    for i in range(11):
        control_sum_2 += int(inn[i]) * coefficients_second[i]
    
    check_digit_2 = control_sum_2 % 11
    if check_digit_2 > 9:
        check_digit_2 %= 10
    
    return check_digit_2 == int(inn[11])


# ========== ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ ==========
if __name__ == "__main__":
    test_inns = [
        ("7712345678", False),   # пример 10-значного ИНН
        ("123456789012", False), # невалидный 12-значный
        ("1234567890", False),   # невалидный 10-значный
        ("000000000000", False), # нули
        ("123", False),          # слишком короткий
        ("1234567890123", False),# слишком длинный
        ("12 34567890", False),  # с пробелами
    ]
    
    print("=== ПРОВЕРКА ФУНКЦИИ ВАЛИДАЦИИ ИНН ===\n")
    for inn_str, expected in test_inns:
        result = validate_inn(inn_str)
        status = "✅" if result == expected else "❌"
        print(f"{status} ИНН: {inn_str:15} -> {result} (ожидалось: {expected})")
