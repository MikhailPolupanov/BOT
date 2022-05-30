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
from emoji import emojize
from datetime import datetime, date, timedelta
from glob import glob  
from random import randint,  choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from datetime import date
import ephem
import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')




def text_emojize(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def greet_user(update, context): 
    text = 'Вызван /start'
    context.user_data['emoji'] = text_emojize(context.user_data)
    print(text)
    update.message.reply_text(
        f'Иди своей дорогой, Сталкер...{context.user_data["emoji"]}',
        reply_markup = my_keyboard()
        )

def word_count(update, text):
    count_text = update.message.text
    words = count_text.split()
    notword = ['!', '?', '.', ',', '@', '#', '$', "%", '^', '&', '*', '(', ')', '"', '-', '+', '-', '??', '???', '????', '!!', '!!!', '!!!!' ,'?!' ,'!?', '..', '...', ':', ';']
    result1 = 0
    result2 = 0
    for word in words:
        for letter in word:
            if letter == '_':
                result1 +=1
            else:
                pass
    for word in words:
        if word in notword:
            result2 += 1
        else:
            pass
            
    if len(words) - 1 == 0:
        update.message.reply_text(f'В сообщении нет слов',
        reply_markup = my_keyboard())
    elif result1 > 0:
        update.message.reply_text(f'Вы используете знак "_". Не делайте так',
        reply_markup = my_keyboard())
    elif result2 > 0:
        update.message.reply_text(f'Вы сделали пробел перед знаком препинания, либо в сообщении нет слов. Не делайте так',
        reply_markup = my_keyboard())
    else:
        update.message.reply_text(len(words)-1,
        reply_markup = my_keyboard())

def talk_to_me(update, context):
    text = update.message.text
    context.user_data['emoji'] = text_emojize(context.user_data)

    print(text)
    if text == "хабар" or text == "Хабар!" or text == "Хабар?":
        update.message.reply_text("Ты бы еще консервных банок насобирал…")
    elif text == "пока" or text == "пока!" or text == "пока?":
        update.message.reply_text("Удачной охоты, сталкер!")
    elif text == "привет" or text == "привет!" or text == "привет?":
        update.message.reply_text("Новичков нынче, как собак нерезаных, и всё-то они лучше стариков знают!")
    elif text == "кто ты"  or text == "кто ты!"  or text == "кто ты?":
        update.message.reply_text("На нас лежит огромная ответственность — нужно защитить мир от наступления Зоны! Свободные сталкеры, ветераны и охотники! Вливайтесь в ряды «Долга»! Защитить мир от заразы Зоны — наша общая цель и задача!")
    elif text == "привет меня зовут Юля" or text == "привет, меня зовут Юля" or text == "Привет, меня зовут Юля!" or text == "меня зовут Юля" or text == "меня зовут Юля" or text == "меня зовут юля" or text == "привет меня зовут юля" or text == "Привет меня зовут Юля" or text == "привет меня зовут Юля" or text == "Привет, меня зовут Юля":
        update.message.reply_text("Женщине не место в зоне")
    elif text == "Что ты умеешь?" or text == "Что ты умеешь" or text == "Что ты можешь" or text == "Что ты можешь?":
        update.message.reply_text("Мочить мутантов")
    else:
        update.message.reply_text(f'{text} {context.user_data["emoji"]}')

def full_moon(update, context):
    user_text = update.message.text
    datetext =  user_text.split()
    date = datetext[1].replace('.', '/')
    moon_date = ephem.next_full_moon(date)
    update.message.reply_text(f'Следующее полнолуние: {moon_date}')

def eph(update, context):
    date_today = date.today()
    planet_text = update.message.text
    planetext = planet_text.split(' ')
    planet = planetext[1]
    print(planet)
    if planetext[1].lower() == 'mars' or planetext[1].lower() == 'марс':
        place = ephem.Mars(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1].lower() == 'mercury' or planetext[1].lower() == 'меркурий':
        place = ephem.Mercury(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1].lower() == 'venus':
        place = ephem.Venus(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con) 
    elif planetext[1].lower() == 'earth':
        place = ephem.Earth(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1].lower() == 'jupiter':
        place = ephem.Jupiter(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1].lower() == 'saturn':
        place = ephem.Saturn(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1].lower() == 'uranus':
        place = ephem.Uranus(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1].lower() == 'neptune':
        place = ephem.Neptune(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1].lower() == 'pluto':
        place = ephem.Pluto(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
    elif planetext[1].lower() == 'sun':
        place = ephem.Sun(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)
    elif planetext[1].lower() == 'moon':
        place = ephem.Moon(date_today)
        place_con = ephem.constellation(place)
        print(place_con)
        update.message.reply_text(place_con)          
    else:
        update.message.reply_text('Такой планеты в солнечной системе нет')

def play_number(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число: {user_number}, моё число: {bot_number}, вы выиграли'
    elif user_number == bot_number:
        message = f'Ваше число: {user_number}, моё число: {bot_number}, ничья'
    else:
        message = f'Ваше число: {user_number}, моё число: {bot_number}, я выиграл'
    return message


def guess_number(update, context):
    print(context.args)
    if context.args: 
        try:
            user_number = int(context.args[0])
            message = play_number(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введите число'
    
    update.message.reply_text(message)

def send_stalker_pict(update, context):
    stalker_photos_list = glob('images/stalker*.jp*g')
    stalker_pic_filename = choice(stalker_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id, photo=open(stalker_pic_filename, 'rb'))
    update.message.reply_text('Я здесь!')
        
def my_keyboard():
    return ReplyKeyboardMarkup([['Кто здесь', 'Узнать где находится планета']])
    
   
  


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("planet", eph))
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(CommandHandler("stalker", send_stalker_pict))
    dp.add_handler(CommandHandler("next_full_moon", full_moon))
    dp.add_handler(MessageHandler(Filters.regex('^(Кто здесь)$'), send_stalker_pict))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
