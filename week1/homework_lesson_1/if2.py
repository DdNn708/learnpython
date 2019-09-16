"""
Домашнее задание №1
Условный оператор: Сравнение строк
* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты
"""


def main(first_string, second_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if isinstance(first_string, str) and isinstance(second_string, str):
        if first_string == second_string:
            return 1
        elif second_string == 'learn':
            return 3
        elif len(first_string) > len(second_string):
            return 2
    else:
        return 0


if __name__ == "__main__":
    for f, s in ("string", "str"), \
                (1, "string"), \
                (1, 1), \
                ("str", "str"), \
                ("string", "learn"), \
                ("str", "learn"), \
                ("string", "fer"):

        result = main(first_string=f, second_string=s)
        print(f'{f}, {s} >>>', result)
