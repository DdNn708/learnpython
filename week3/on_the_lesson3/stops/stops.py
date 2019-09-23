""" Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок,
    вывести улицу, на которой больше всего остановок.

"""

import csv


INPUT_FILE = 'stops/stops_list.csv'
OUTPUT_FILE = 'stops/stops_list_utf8.csv'


def converter():
    """ Переливает содержимое исходного файла в файл с кодировкой utf-8
    """
    with open(INPUT_FILE, 'r', encoding='cp1251') as f_output:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_input:
            for line in f_output:
                f_input.write(line)


def stops_counter(any_name: str, dictionary: dict):
    """ На вход получает строку, и словарь в который записывает результаты подсчета.
        Проверяет наличие в словаре строки.
        Если строка есть, то увеличивает счетчик на 1.
        Если строки нет, то создает ключ с названием строки и присваивает значение 1.
    """
    if not dictionary.get(any_name):
        dictionary[any_name] = 1
    else:
        dictionary[any_name] += 1


if __name__ == '__main__':
    # converter()

    # Создаем пустой словарь, в который будем записывать результаты подсчета
    count_result = {}

    with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
        # Разбиваем первую строку на список, очищая от символов '"' двойных кавычек, признаков начала и окончания значения.
        fields = []
        for line in f:
            fields = line.split(';')
            break
        fields = list(map(lambda x: x.strip('"'), fields))

        # Вывод первой строки, исключительно для удобства восприятия
        print(fields, "\n")

        reader = csv.DictReader(f, fields, delimiter=';', quotechar='"')

        # # Код позволяет посмотреть определенное количество строк в файле, а не все сразу
        # # Необходимо только на этапе написания программы
        # for _, row in zip(range(10), reader):
        #     print(row)

        # Идем по файлы с данными построчно, и из каждой строки передаем в функция счетчик параметр,
        # по которому ведем подсчет
        for row in reader:
            stops_counter(
                any_name=row['Street'],     # параметр по которому ведем подсчет
                dictionary=count_result)    # словрь в который пишем результат подсчета

        # Так можем вывести построчно все данные из предварительно отсортированного словаря со счетчиками
        # for street in sorted(count_result.items(), key=lambda x: x[1], reverse=True):
        #     print(street)

        # Так можем вывести в виде списка все данные из предварительно отсортированного словаря со счетчиками
        # print(sorted(count_result.items(), key=lambda x: x[1], reverse=True))

        # Так можем вывести самую первую запись из отсортированного по значениям счетчика словаря
        print(next(iter(dict(sorted(count_result.items(), key=lambda x: x[1], reverse=True)).items())))

    # Так можно представить работу функции 'lambda x: x.strip('"')'
    # def something(x):
    #     return x.strip('"')
