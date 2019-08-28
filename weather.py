import pyowm
from datetime import datetime, timedelta
from constants import api_key_pyowm, city

owm = pyowm.OWM(api_key_pyowm, language='ru')
obs = owm.weather_at_place(city)
w = obs.get_weather()
ad = w.get_pressure()['press']
adrs = round(ad / 1.333224)
fc = owm.three_hours_forecast(city)
f = fc.get_forecast()
time_r_obs = w.get_sunrise_time('date')
time_r = time_r_obs + timedelta(hours=3)
time_s_obs = w.get_sunset_time('date')
time_s = time_s_obs + timedelta(hours=3)
date_tomorrow = datetime.now() + timedelta(days=1)
date_in_2_days = datetime.now() + timedelta(days=2)
date_in_3_days = datetime.now() + timedelta(days=3)
date_in_4_days = datetime.now() + timedelta(days=4)


def answer_now_w():
    answer = "Сейчас в Минске {0} {1}, {2}\nВлажность: {3} %\nСкорость ветра: {4} м/с\n" \
             "Атмосферное давление: {5} гПА,\nили {6} мм.рт.ст\nВремя восхода: {7}\nВремя заката: {8}".format(
        round(w.get_temperature('celsius')['temp']),
        u'\u2103',
        w.get_detailed_status(),
        w.get_humidity(),
        w.get_wind()['speed'],
        ad,
        adrs,
        time_r.strftime('%H:%M:%S'),
        time_s.strftime('%H:%M:%S')
    )
    return answer


def answer_today_f(f):
    answer = '{}\n'.format(datetime.now().strftime('%d.%m.%Y'))
    for weather in f:
        time_obs = weather.get_reference_time('date')
        time_minsk = time_obs + timedelta(hours=3)
        if time_minsk.day == datetime.now().day:
            answer_str = "{0}   {1} {2}, {3}".format(
                time_minsk.strftime('%H:%M'),
                round(weather.get_temperature('celsius')['temp']),
                u'\u2103',
                weather.get_detailed_status(),
            )
            answer += answer_str + '\n'
    return answer


def answer_tomorrow_f(f):
    answer = '{}\n'.format(date_tomorrow.strftime('%d.%m.%Y'))
    for weather in f:
        time_obs = weather.get_reference_time('date')
        time_minsk = time_obs + timedelta(hours=3)
        if time_minsk.day == date_tomorrow.day:
            answer_str = "{0}   {1} {2}, {3}".format(
                time_minsk.strftime('%H:%M'),
                round(weather.get_temperature('celsius')['temp']),
                u'\u2103',
                weather.get_detailed_status(),
            )
            answer += answer_str + '\n'
    return answer


def answer_in_2_days_f(f):
    answer = '{}\n'.format(date_in_2_days.strftime('%d.%m.%Y'))
    for weather in f:
        time_obs = weather.get_reference_time('date')
        time_minsk = time_obs + timedelta(hours=3)
        if time_minsk.day == date_in_2_days.day:
            answer_str = "{0}   {1} {2}, {3}".format(
                time_minsk.strftime('%H:%M'),
                round(weather.get_temperature('celsius')['temp']),
                u'\u2103',
                weather.get_detailed_status(),
            )
            answer += answer_str + '\n'
    return answer


def answer_in_3_days_f(f):
    answer = '{}\n'.format(date_in_3_days.strftime('%d.%m.%Y'))
    for weather in f:
        time_obs = weather.get_reference_time('date')
        time_minsk = time_obs + timedelta(hours=3)
        if time_minsk.day == date_in_3_days.day:
            answer_str = "{0}   {1} {2}, {3}".format(
                time_minsk.strftime('%H:%M'),
                round(weather.get_temperature('celsius')['temp']),
                u'\u2103',
                weather.get_detailed_status(),
            )
            answer += answer_str + '\n'
    return answer


def answer_in_4_days_f(f):
    answer = '{}\n'.format(date_in_4_days.strftime('%d.%m.%Y'))
    for weather in f:
        time_obs = weather.get_reference_time('date')
        time_minsk = time_obs + timedelta(hours=3)
        if time_minsk.day == date_in_4_days.day:
            answer_str = "{0}   {1} {2}, {3}".format(
                time_minsk.strftime('%H:%M'),
                round(weather.get_temperature('celsius')['temp']),
                u'\u2103',
                weather.get_detailed_status(),
            )
            answer += answer_str + '\n'
    return answer


answer_3_days = '{0}\n{1}\n{2}'.format(
    answer_today_f(f),
    answer_tomorrow_f(f),
    answer_in_2_days_f(f)
)

answer_5_days = '{0}\n{1}\n{2}\n{3}\n{4}'.format(
    answer_today_f(f),
    answer_tomorrow_f(f),
    answer_in_2_days_f(f),
    answer_in_3_days_f(f),
    answer_in_4_days_f(f),
)
