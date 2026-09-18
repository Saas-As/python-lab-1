#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# Создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код

garden_set = set(garden)
meadow_set = set(meadow)

# Выведите на консоль все виды цветов
# TODO здесь ваш код


# Выведите на консоль те, которые растут и там и там
# TODO здесь ваш код



# Выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код



# Выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код

def flowers_analysis(garden, meadow):
    g = set(garden)
    m = set(meadow)
    return g | m, g & m, g - m, m - g


def run():
    all_f, common, only_garden, only_meadow = flowers_analysis(garden, meadow)
    print('Все виды:', all_f)
    print('И там, и там:', common)
    print('Только в саду:', only_garden)
    print('Только на лугу:', only_meadow)


if __name__ == '__main__':
    run()