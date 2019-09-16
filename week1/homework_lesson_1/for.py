"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    academic_performance = [
        {'school_class': '3b', 'scores': [3, 3, 4, 5, 2]},
        {'school_class': '4a', 'scores': [4, 2, 4, 5, 1]},
        {'school_class': '5d', 'scores': [1, 4, 5, 5, 3]},
        {'school_class': '5a', 'scores': [5, 5, 4, 5, 4]},
        {'school_class': '5c', 'scores': [2, 4, 3, 3, 3]},
    ]

    all_scores = 0
    sum_scores = 0
    for school_class in academic_performance:
        all_scores += len(school_class['scores'])
        sum_scores += sum(school_class['scores'])

    print('\n')
    print(f'Средний балл по всем классам в школе: {sum_scores / all_scores}')
    print('----------')

    for school_class in academic_performance:
            average_rating = sum(school_class["scores"])/len(school_class["scores"])
            _class = school_class["school_class"]
            print(f'Средняя оценка {_class} класса: {average_rating}')


if __name__ == "__main__":
    main()




