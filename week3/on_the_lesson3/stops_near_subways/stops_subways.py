""" Остановки у метро.
    Объединить наборы данных из предыдущих задач и посчитать,
    у какой станции метро больше всего остановок (в радиусе 0.5 км).
"""

import csv
import json

from datetime import datetime
from geopy import distance

STOPS = '/Users/dnv/projects/learnpython/week3/on_the_lesson3/stops/stops_list_utf8.csv'
SUBWAY = '/Users/dnv/projects/learnpython/week3/on_the_lesson3/subway_repair/data_utf8.json'


def distance_calculation(geo_point1: tuple, geo_point2: tuple):
    return float(distance.distance(geo_point1, geo_point2).km)


def subway_counter(any_name: str, dictionary: dict):
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
    start = datetime.now()
    print(f'Скрипт начал работу в: {start}')
    count_result = {}
    with open(SUBWAY, 'r', encoding='utf-8') as f:
        subway_data = json.load(f)

        for row_subway in subway_data:
            if row_subway['geoData']['coordinates']:
                subway_coordinates = tuple(row_subway['geoData']['coordinates'])

            with open(STOPS, 'r', encoding='utf-8') as k:
                fields = next(k).split(';')
                fields = list(map(lambda x: x.strip('"'), fields))
                reader_stops_data = csv.DictReader(k, fields, delimiter=';', quotechar='"')

                for dictionary in reader_stops_data:
                    if len(str(dictionary['geoData'])) > 7:
                        stop_coordinates = str(dictionary['geoData']).replace('{type=Point, coordinates=[', '')
                        stop_coordinates = stop_coordinates.replace(']}', '').split(', ')
                        stop_coordinates = tuple(map(float, stop_coordinates))

                        station_distance = distance_calculation(subway_coordinates, stop_coordinates)
                        if station_distance <= 0.5:
                            # print(row_subway['Name'], station_distance)
                            subway_counter(row_subway['Name'], count_result)

    # Так можем вывести построчно все данные из предварительно отсортированного словаря со счетчиками
    for station_name in sorted(count_result.items(), key=lambda x: x[1], reverse=True):
        print(station_name)

    stop = datetime.now()
    print(f'Скрипт начал работу в: {start}')
    print(f'Скрипт закончил работу в: {stop}')

    # Скорость выполнения
    # Скрипт начал работу в: 2019-09-23 06:23:12.734174
    # Скрипт закончил работу в: 2019-09-23 07:07:56.778101

    # Часть верхних строк с результатом
    # ('Юго-Западная, вход-выход 3 в южный вестибюль', 32)
    # ('Юго-Западная, вход-выход 4 в южный вестибюль', 32)
    # ('Юго-Западная, вход-выход 1 в южный вестибюль', 32)
    # ('Юго-Западная, вход-выход 2 в южный вестибюль', 32)
    # ('Юго-Западная, вход-выход 3 в северный вестибюль', 31)
    # ('Юго-Западная, вход-выход 4 в северный вестибюль', 31)
    # ('Юго-Западная, вход-выход 2 в северный вестибюль', 29)
    # ('Юго-Западная, вход-выход 1 в северный вестибюль', 28)
    # ('Новогиреево, вход-выход 1 в западный вестибюль', 28)
    # ('Новогиреево, вход-выход 4 в западный вестибюль', 27)
    # ('Выставочный центр, вход-выход в вестибюль', 26)
    # ('Новогиреево, вход-выход 3 в восточный вестибюль', 26)
    # ('Новогиреево, вход-выход 1 в восточный вестибюль', 25)
    # ('Семеновская, вход в вестибюль', 25)
    # ('Семеновская, выход из вестибюля', 25)
    # ('Алтуфьево, вход-выход 4 в северный вестибюль', 25)
    # ('Алтуфьево, вход-выход 3 в северный вестибюль', 25)
    # ('Марксистская, вход-выход 2 в вестибюль', 24)
    # ('Марксистская, вход-выход 1 в вестибюль', 24)
    # ('Таганская, вход-выход 2 в вестибюль', 24)