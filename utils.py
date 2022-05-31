import settings
from emoji import emojize
from random import randint, choice
from telegram import ReplyKeyboardMarkup, KeyboardButton

def text_emojize(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def play_number(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число: {user_number}, моё число: {bot_number}, вы выиграли'
    elif user_number == bot_number:
        message = f'Ваше число: {user_number}, моё число: {bot_number}, ничья'
    else:
        message = f'Ваше число: {user_number}, моё число: {bot_number}, я выиграл'
    return message

def my_keyboard():
    return ReplyKeyboardMarkup([['Кто здесь', KeyboardButton('Мои координаты', request_location = True)]])