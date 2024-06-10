import json

def employees_rewrite(sort_type):
    # Привести ключ к нижнему регистру для унификации
    sort_key = sort_type

    # Прочитать данные из JSON-файла
    try:
        with open('employees.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            employees = data['employees']
    except FileNotFoundError:
        print("Файл employees.json не найден.")
        return
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON.")
        return

    # Проверка наличия ключа в данных
    if not employees or sort_key not in employees[0]:
        raise ValueError("Bad key for sorting")

    # Определение типа значений по ключу
    if isinstance(employees[0][sort_key], str):
        reverse = False
    elif isinstance(employees[0][sort_key], (int, float)):
        reverse = True
    else:
        raise ValueError("Unsupported key type for sorting")

    # Сортировка данных по заданному ключу
    sorted_employees = sorted(employees, key=lambda x: x[sort_key], reverse=reverse)

    # Запись отсортированных данных в новый JSON-файл
    output_filename = f'employees_{sort_type}_sorted.json'
    with open(output_filename, 'w', encoding='utf-8') as file:
        json.dump({'employees': sorted_employees}, file, ensure_ascii=False, indent=2)

# Пример использования функции
employees_rewrite('lastName')
