import telebot
from datetime import datetime
from constants import token, answer_plug
from weather import answer_now_w, f, answer_today_f, answer_tomorrow_f, answer_3_days, answer_5_days

bot = telebot.TeleBot(token)

print(bot.get_me())


def log(message, answer):
    print("\n----------")
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \nТекст: {3}".format(
        message.from_user.first_name,
        message.from_user.last_name,
        str(message.from_user.id),
        message.text
    ))
    print("Ответ:", answer)


@bot.message_handler(commands=['start'])
def handle_start(message):
    answer = "Добро пожаловать \nВыберите пункт"
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('Погода сейчас')
    user_markup.row('Прогноз на сегодня', 'Прогноз на завтра')
    user_markup.row('Прогноз на 3 дня', 'Прогноз на 5 дней')
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)
    log(message, answer)


@bot.message_handler(commands=['stop'])
def handle_start(message):
    answer = "До встречи! \nХотите вызвать меню нажмите /start"
    hide_markup = telebot.types.ReplyKeyboardRemove(True)
    bot.send_message(message.from_user.id, answer, reply_markup=hide_markup)
    log(message, answer)


@bot.message_handler(content_types=['text'])
def handle_start2(message):
    if message.text == 'Погода сейчас':
        bot.send_message(message.from_user.id, answer_now_w())
        log(message, answer_now_w())
    elif message.text == 'Прогноз на сегодня':
        bot.send_message(message.from_user.id, answer_today_f(f))
        log(message, answer_today_f(f))
    elif message.text == 'Прогноз на завтра':
        bot.send_message(message.from_user.id, answer_tomorrow_f(f))
        log(message, answer_tomorrow_f(f))
    elif message.text == 'Прогноз на 3 дня':
        bot.send_message(message.from_user.id, answer_3_days)
        log(message, answer_3_days)
    elif message.text == 'Прогноз на 5 дней':
        bot.send_message(message.from_user.id, answer_5_days)
        log(message, answer_5_days)
    else:
        bot.send_message(message.from_user.id, answer_plug)
        log(message, answer_plug)


bot.polling(none_stop=True, interval=0)
