#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)


# список списков приблизительного роста членов вашей семьи


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

# TODO здесь ваш код

my_family = ['я', 'мама', 'папа']
my_family_height = [
    ['я', 180],
    ['мама', 170],
    ['папа', 172],
]


def get_father_height(family_height):
    for member in family_height:
        if member[0] == 'папа':
            return member[1]


def get_total_height(family_height):
    return sum(member[1] for member in family_height)


def run():
    print(f'Рост отца - {get_father_height(my_family_height)} см')
    print(f'Общий рост моей семьи - {get_total_height(my_family_height)} см')


if __name__ == '__main__':
    run()