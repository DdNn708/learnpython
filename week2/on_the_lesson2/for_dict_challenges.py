

def name_counter(school_class: list):  # Fixme этот не оптимален по асимптотике
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


def name_counter_v2(list_with_dicts: list):  # Fixme этот тож так себе
    """Функция счетает повторяющиеся имена и складывает результаты в словарь, где key это имя,
        а value это количество повторений"""
    count_result = {}

    for element in list_with_dicts:
        for key, value in element.items():
            if bool(count_result.get(value)):
                count_result[value] += 1
            else:
                count_result[value] = count_result.get(value, 1)
    return count_result  # dict with results


def count_names_v3(students: list):
    count_result = {}
    for student in students:
        if student['first_name'] in count_result:
            count_result[student['first_name']] += 1
        else:
            count_result[student['first_name']] = 1
    return count_result  # dict with results


def get_most_frequent_name(dictionary: dict):
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

count_result = count_names_v3(students)


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

count_result = count_names_v3(students)

# Что бы перед глазами был результат частотного анализа
for key, value in count_result.items():
    print(key, ": ", value)

most_frequent_name = dict(sorted(count_result.items(), key=lambda name: name[1], reverse=True))
print(f"Самое частое имя среди учеников: {next(iter(most_frequent_name))}")

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

for class_num, element in enumerate(school_students, 1):
    count_result = count_names_v3(element)
    most_frequent_name = dict(sorted(count_result.items(), key=lambda name: name[1], reverse=True))
    print(f"Самое частое имя в классе {class_num}: {next(iter(most_frequent_name))}")

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


for school_class in school:
    m_counter = 0
    f_counter = 0
    for student in school_class['students']:
        print(student)
        if is_male[student['first_name']]:
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
    print(school_class)
    for element in school_class.items():
        pass
        # most_frequent_name = dict(sorted(element['gender'], key=lambda name: name[1], reverse=True))
    # print(most_frequent_name)
    # gender = most_frequent_names(school_class['gender'])
    # if 'female' in gender:
    #     print(f'Больше всего девочек в классе {school_class["class"]}')
    # else:
    #     print(f'Больше всего мальчиков в классе {school_class["class"]}')


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
