""" В этом задании требуется определить, на каких станциях московского метро сейчас идёт ремонт эскалаторов и вывести на экран их названия.
    Файл с данными можно скачать на странице http://data.mos.ru/opendata/624/row/1773539.
"""

import json
from datetime import datetime


INPUT_FILE = 'data.json'
OUTPUT_FILE = 'data_utf8.json'


def converter():
    """ Переливает содержимое исходного файла в файл с кодировкой utf-8 """
    with open(INPUT_FILE, 'r', encoding='cp1251') as f_output:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_input:
            for line in f_output:
                f_input.write(line)


def date_entry_check(string_with_time: str):
    time_in_list: list = string_with_time.split('-')
    today = datetime.today()
    date1 = datetime.strptime(time_in_list[0], '%d.%m.%Y')
    date2 = datetime.strptime(time_in_list[1], '%d.%m.%Y')
    if date1 <= today <= date2:
        return True
    else:
        return False


if __name__ == '__main__':
    # converter()

    with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print('\n')

    # Что бы посмотреть все параметры для станций на которых заполнен параметр 'RepairOfEscalators'
    # for row in data:
    #     if row['RepairOfEscalators']:
    #         for key, value in row.items():
    #             print(key, ": ", value)
    #         print("========================\n")

    for row in data:
        if row['RepairOfEscalators']:
            if date_entry_check(row['RepairOfEscalators'][0]['RepairOfEscalators']):
                print(f"Сейчас на станции \"{row['Name']}\" ведутся работы")
            else:
                print(f"На станции \"{row['Name']}\" велись работы: {row['RepairOfEscalators'][0]['RepairOfEscalators']}")

