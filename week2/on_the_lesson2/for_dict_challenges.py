

def name_counter(school_class: list):
    """Функция счетает повторяющиеся имена и складывает результаты в словарь, где key это имя,
    а value это количество повторений"""
    count_result = {}
    matching_map = [False] * len(school_class)

    # Поочереди берем каждое имя в списке и сравниваем его со всеми именами в списке
    # Если найдено соответствующее значение записываем в список matching_map значение False
    for i in range(len(school_class)):

        # Позиция которую сравниваем с остальными в списке
        name = school_class[i]['first_name']

        # Перебирая список словарей сравниваем зафиксированную позицию
        for k in range(len(school_class)):

            # Если в словаре есть соответствующая позиция и в карте матчинга отсутствует True, то заходим в if
            if name == school_class[k]['first_name'] and matching_map[k] is False:
                count_result[school_class[k]['first_name']] = count_result.get(school_class[k]['first_name'], 0) + 1
                matching_map[k] = True
    return count_result  # dict


def most_frequent_names(dictionary: dict):
    """Функция находит максимальное значение среди values и возвращает key"""
    max_value = 0
    max_key = ""
    for key, value in dictionary.items():
        if max_value < value:
            max_value = value
            max_key = key

    return max_key


# Задание 1
print('\n')
print("--------Задание 1--------")
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

count_result = name_counter(students)

for key, value in count_result.items():
    print(key, ": ", value)

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
print('\n')
print("--------Задание 2--------")
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

count_result = name_counter(students)

# Что бы перед глазами был результат частотного анализа
for key, value in count_result.items():
    print(key, ": ", value)

max_key = most_frequent_names(count_result)
print(f"Самое частое имя среди учеников: {max_key}")

# Пример вывода:
# Самое частое имя среди учеников: Маша


# Задание 3
print('\n')
print("--------Задание 3--------")
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]


print(school_students)
for i in range(len(school_students)):
    count_result_in_dict = name_counter(school_students[i])
    most_frequent_name = most_frequent_names(count_result_in_dict)
    print(f"Самое частое имя в классе {i+1}: {most_frequent_name}")


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
#

# Задание 4
print('\n')
print("--------Задание 4--------")
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


def gender_definer(first_name: str):
    pass
    # for i in range(len(names)):
    #     if is_male[names[i]]:
    #         print(f"{names[i]} пол: муж")
    #     else:
    #         print(f"{names[i]} пол: жен")


for school_class in school:
    m_counter = 0
    f_counter = 0
    for students in school_class['students']:
        print(students)
        if is_male[students['first_name']]:
            m_counter += 1
        else:
            f_counter += 1

    print(f'В классе {school_class["class"]} {f_counter} девочки и {m_counter} мальчика.')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
print('\n')
print("--------Задание 5--------")
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]

is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for school_class in school:
    school_class['gender'] = {'female': 0, 'male': 0}
    for students in school_class['students']:
        if is_male[students['first_name']]:
            school_class['gender']['male'] += 1
        else:
            school_class['gender']['female'] += 1

for school_class in school:
    print(most_frequent_names(school_class['gender']))
    gender = most_frequent_names(school_class['gender'])
    if 'female' in gender:
        print(f'Больше всего девочек в классе {school_class["class"]}')
    else:
        print(f'Больше всего мальчиков в классе {school_class["class"]}')


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a