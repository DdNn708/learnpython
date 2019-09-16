"""
Домашнее задание №1
Цикл while: ask_user
* Напишите функцию ask_user(), которая с помощью input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        user_ask = input("Как дела? ")
        user_ask = user_ask.strip().lower()
        if user_ask == "хорошо":
            print("Раз хорошо, то пока")
            break
        else:
            continue


if __name__ == "__main__":
    ask_user()

