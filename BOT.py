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
import logging
from anketa import anketa_start, anketa_name, anketa_rating, anketa_skip, anketa_comment, anketa_dontknow
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import settings
from handlers import (greet_user, talk_to_me, guess_number, send_stalker_pict, 
                        user_coordinates, word_count, full_moon, eph, check_user_photo, photo_request)

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher

    anketa = ConversationHandler(
		entry_points = [MessageHandler(Filters.regex('^(Заполнить анкету)$'), anketa_start)],
		states = {
        'name': [MessageHandler(Filters.text, anketa_name)],
        'rating': [MessageHandler(Filters.regex('^(1|2|3|4|5)$'), anketa_rating)],
        'comment': [CommandHandler('skip', anketa_skip), MessageHandler(Filters.text, anketa_comment)]
		},
		fallbacks = [
			MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location, anketa_dontknow)
		]
    )
    dp.add_handler(anketa)
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("planet", eph))
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(CommandHandler("stalker", send_stalker_pict))
    dp.add_handler(CommandHandler("next_full_moon", full_moon))
    dp.add_handler(MessageHandler(Filters.regex('^(Отправить картинку)$'), photo_request))
    dp.add_handler(MessageHandler(Filters.photo, check_user_photo))
    dp.add_handler(MessageHandler(Filters.regex('^(Кто здесь)$'), send_stalker_pict))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
