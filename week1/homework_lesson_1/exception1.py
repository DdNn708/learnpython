"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break

"""


def ask_user(answers):
    """
    Замените pass на ваш код
    """
    while True:
        try:
            user_ask = input("Пользователь: ")
        except (KeyboardInterrupt, EOFError):
            print("Пока!")
            break

        user_ask = user_ask.strip().capitalize()
        if user_ask in answers:
            print("Программа: " + answers.get(user_ask))


if __name__ == "__main__":
    the_answers = {
        'Как дела?': 'Отлично!',
        'Что делаешь?': 'Варю варенье',
        'Какие планы на вечер?': 'Встречаюсь со знакомым.',
        'Давай созвонимся на выходных': 'Можно и встретиться'
    }
    ask_user(the_answers)
