"""
Домашнее задание №1
Цикл while: ask_user со словарём
* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит
  пользователя ввести вопрос, а затем, если вопрос есть в словаре,
  программа давала ему соотвествующий ответ. Например:
    Пользователь: Что делаешь?
    Программа: Программирую

"""


def ask_user(answers):
    """
    Замените pass на ваш код
    """
    while True:
        user_ask = input("Пользователь: ")
        user_ask = user_ask.strip().capitalize()
        if user_ask in answers:
            print("Программа: " + answers.get(user_ask))
        else:
            print("Не знаю что ответить")
            break


if __name__ == "__main__":
    the_answers = {
        'Как дела?': 'Отлично!',
        'Что делаешь?': 'Варю варенье',
        'Какие планы на вечер?': 'Встречаюсь со знакомым.',
        'Давай созвонимся на выходных': 'Можно и встретиться'
    }
    ask_user(the_answers)

