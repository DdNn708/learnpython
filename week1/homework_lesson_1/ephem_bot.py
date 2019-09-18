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
# import sys
# sys.path.append('/Users/dnv/projects/learnpython/week1/homework_lesson_1/settings.py')
# print(sys.path)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
import ephem
import logging
import settings  # Fixme как добавить модуль в область видимости импорта


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

    # text = 'Вызван /start'  # Добавляет текст в консоль
    # print(update)
    # logging.info(text)


def talk_to_me(bot, update):
    # похож на объект типа ключ-значение
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)

    # Логгируем кто и что нам написал
    logging.info("User: %s, Chat id: %s, Message: %s",
                 update.message.chat.username,
                 update.message.chat.id,
                 update.message.text)

    update.message.reply_text(user_text)


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info("Бот запускается")

    # Диспетчер принимает вхожящие и раскидывает по соответствующим получателям
    dp = mybot.dispatcher

    # Если пришла команда start, то вызвать определенную функцию
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", greet_user))

    # Указываем на какой тип сообщений необходимо реагировать и какую функцию при этом использовать
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()  # регулярно ходим на платформу телеграм и проверяем сообщения
    mybot.idle()  # mybot будет работать принудительно пока мы его принудительно не остановим


if __name__ == "__main__":
    main()


