# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

count_result = {}
matching_map = [False] * len(students)

for i in range(len(students)):
    name = students[i]['first_name']
    for k in range(len(students)):
        if name == students[k]['first_name'] and matching_map[k] is False:
            count_result[students[k]['first_name']] = count_result.get(students[k]['first_name'], 0) + 1
            matching_map[k] = True

for key, value in count_result.items():
    print(key, ": ", value)
print("------------------")

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

count_result = {}
matching_map = [False] * len(students)

for i in range(len(students)):
    name = students[i]['first_name']
    for k in range(len(students)):
        if name == students[k]['first_name'] and matching_map[k] is False:
            count_result[students[k]['first_name']] = count_result.get(students[k]['first_name'], 0) + 1
            matching_map[k] = True

for key, value in count_result.items():
    print(key, ": ", value)

max_value = 0
max_key = ""
for key, value in count_result.items():
    if max_value < value:
        max_value = value
        max_key = key

print(f"Самое частое имя среди учеников: {max_key}")
print("------------------")

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
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


def name_counter(school_class: list):
    count_result = {}
    matching_map = [False] * len(school_class)

    for i in range(len(school_class)):
        name = school_class[i]['first_name']
        for k in range(len(school_class)):
            if name == school_class[k]['first_name'] and matching_map[k] is False:
                count_result[school_class[k]['first_name']] = count_result.get(school_class[k]['first_name'], 0) + 1
                matching_map[k] = True
    return count_result


def most_frequent_names(dictionary: dict):
    max_value = 0
    max_key = ""
    for key, value in dictionary.items():
        if max_value < value:
            max_value = value
            max_key = key

    return max_key


print(school_students)
for i in range(len(school_students)):
    count_result_in_dict = name_counter(school_students[i])
    most_frequent_name = most_frequent_names(count_result_in_dict)
    print(f"Самое частое имя в классе {i+1}: {most_frequent_name}")

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4  # FIXME
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
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
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
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a