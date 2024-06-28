"""
Домашнее задание №1
Использование библиотек: ephem
* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
import ephem
import logging
import settings

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)


def greet_user(bot, update):  # При помощи первого параметра, мы сможем отдавать боту команды
    if str(update.message.text).split()[1]:
        planet = str(update.message.text).split()[1].capitalize()
        today_date = datetime.today().strftime('%Y/%m/%d')
        request_to_ephem = f"ephem.{planet}('{today_date}')"
        planet_info = ephem.constellation(eval(request_to_ephem))
        update.message.reply_text("Сегодня {} в созвезддии: {}".format(planet, planet_info[1]))


def talk_to_me(bot, update):
    # похож на объект типа ключ-значение
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)

    # Логгируем кто и что нам написал
    logging.info("User: %s, Chat id: %s, Message: %s",
                 update.message.chat.username,
                 update.message.chat.id,
                 update.message.text)

    update.message.reply_text(user_text)


def count_words(bot, update):
    """ Реализуйте в боте команду /wordcount
        которая считает слова в присланной фразе.
        Например на запрос /wordcount Привет как дела бот должен ответить: 3 слова.
        Не забудьте:
        - Добавить проверки на пустую строку
        - Как можно обмануть бота, какие еще проверки нужны?
    """
    count = update.message.text.split()[1:]
    print(count)
    count = len(count)
    if count == 0:
        update.message.reply_text(f"Здесь нет слов")
    else:
        update.message.reply_text(f"{count} слова")


def get_next_full_moon(bot, update):
    """ Реализуйте в боте команду,
        которая отвечает на вопрос “Когда ближайшее полнолуние?”
        Например /next_full_moon 2019-01-01.
        Чтобы узнать, когда ближайшее полнолуние,
        используйте ephem.next_full_moon(ДАТА)
    """
    today = datetime.today().strftime('%Y/%m/%d')
    update.message.reply_text(f"Ближайшее полнолуние будет {ephem.next_full_moon(today)}")


def cities_game(bot, update):  # Fixme города пока что не работают
    """ Научите бота играть в города.
        Правила такие - внутри бота есть список городов,
        пользователь пишет /cities Москва и если в списке такой город есть,
        бот отвечает городом на букву "а" - "Альметьевск, ваш ход".
        Оба города должны удаляться из списка.
        Помните, с ботом могут играть несколько пользователей одновременно
    """


    # rule = 'Игра началась! Далее в сообщения можно указывать просто города, без "/cities" \
    #         Что бы закончить игру, необходимо написать "q". \
    #         Для начала, назовите любой город России.'
    # update.message.reply_text(rule)

    # user_text = str(update.message.text).strip().split()[1:]
    # user_text = str(user_text[0]).capitalize()
    # game = []
    # user_text = ""
    # while 'q' != user_text:
    #     # dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    #     user_text = str(Filters.text).strip().capitalize()
    #     print(user_text)

    # if user_text in cities_list:
    #     if len(game) == 0:
    #         game.append(user_text)
    #         update.message.reply_text(f'Следующий город на букву "{str(game[-1])[-1].upper()}"')
    #         continue
    #     elif user_text not in game and user_text[0].lower() == str(game[-1])[-1]:
    #             print(user_text[0].lower(), str(game[-1])[-1])
    #             game.append(user_text)
    #             update.message.reply_text(f'Защитано! Такого города еще не называли.\n Следующий город на букву "{str(game[-1])[-1].upper()}"')
    #             continue
    #     else:
    #         update.message.reply_text(f'Жааааль, но город "{user_text}" уже называли')
    # else:
    #     update.message.reply_text(f'Должно быть вы ошиблись, у меня в списке нет такого слова "{user_text}"')
    # print(game)


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info("Бот запускается")

    # Диспетчер принимает вхожящие и раскидывает по соответствующим получателям
    dp = mybot.dispatcher

    # Если пришла команда start, то вызвать определенную функцию
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", greet_user))
    dp.add_handler(CommandHandler("wordcount", count_words))
    dp.add_handler(CommandHandler("next_full_moon", get_next_full_moon))
    # dp.add_handler(CommandHandler("cities", cities_game))

    # Указываем на какой тип сообщений необходимо реагировать и какую функцию при этом использовать
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()  # регулярно ходим на платформу телеграм и проверяем сообщения
    mybot.idle()  # mybot будет работать принудительно пока мы его принудительно не остановим


if __name__ == "__main__":
    main()
