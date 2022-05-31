# Проект Polupanobot

Polupanobot - это бот для Telegram, который умеет делать всякую ненужную хрень

## Установка

1. Клонируйте репозиторий c https://github.com/MikhailPolupanov/BOT.git
2. Создайте виртуальное окружение
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте файл `settings.py`
5. Впишите в settings.py переменные 
```
API_KEY = "API-ключ бота"
USER_EMOJI = [':running:', ':boar:', ':gun:', ':alien:', ':sunny:', ':last_quarter_moon_with_face:']
```
6. Запустите бота командой `python bot.py`

### Что умеет делать бот

1. Бот может вас послать, если вы введете команду `/start`
2. Бот может в вас пульнуть картинкой из Сталкера, если вы нажмете на кнопку `Кто здесь`
3. Бот может поиграть с вами в игру "числа". Напишите своё целое число после команды `/guess` и повезет либо вам, либо боту
4. Бот может сообщить ваши координаты, если вы нажмете на кнопку `Мои координаты`
5. Бот умеет считать кол-во слов, которые вы укажете после команды `/wordcount`. Не пытайтесь его обмануть, у вас не получится. Хотя может и получится
6. Не спрашивайте зачем, но бот может сообщать дату следующего полнолуния по команде `/next_full_moon`. При этом дату, от которой бот выдаст следующую дату затмения, нужно писать в таком формате `yyyy.mm.dd`
7. Ну и любимая функция моей жены: бот может сообщать в каком созведнии находятся планеты Солнечной системы на данный момент. Для этого введите `/planet` и название планеты на английском языке. Для Марса работает и на русском, но дальше мне стало лень писать. Пробить Землю не пытайтесь - ведь мы смотрим с Земли на планеты!
