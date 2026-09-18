#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что суммирование чисел с плавающей точкой может давать погрешность,
# округлите результат до 3 знаков после запятой
# TODO здесь ваш код


# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# Распечатайте общее время звучания трех других песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
# в формате
#   А другие три песни звучат ХХХ минут
# Обратите внимание на округление
# TODO здесь ваш код

def songs_time_from_list(songs_list, names):
    return round(sum(s[1] for s in songs_list if s[0] in names), 3)


def songs_time_from_dict(songs_dict, names):
    return round(sum(songs_dict[n] for n in names), 3)


def run():
    t1 = songs_time_from_list(violator_songs_list, ['Halo', 'Enjoy the Silence', 'Clean'])
    print(f'Три песни звучат {t1} минут')

    t2 = songs_time_from_dict(violator_songs_dict, ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'])
    print(f'А другие три песни звучат {t2} минут')


if __name__ == '__main__':
    run()