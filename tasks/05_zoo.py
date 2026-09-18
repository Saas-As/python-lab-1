#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Посадите медведя (bear) между львом и кенгуру
# и выведите список на консоль
# TODO здесь ваш код



# Добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
# и выведите список на консоль
# TODO здесь ваш код



# Уберите слона (elephant) из зоопарка
# и выведите список на консоль
# TODO здесь ваш код



# Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).
# TODO здесь ваш код

def build_zoo(zoo, birds):
    zoo.insert(1, 'bear')
    zoo.extend(birds)
    zoo.remove('elephant')
    return zoo


def get_cell(zoo, animal):
    return zoo.index(animal) + 1


def run():
    result = build_zoo(zoo, birds)
    print(result)
    print(f'Лев в клетке №{get_cell(result, "lion")}')
    print(f'Жаворонок в клетке №{get_cell(result, "lark")}')


if __name__ == '__main__':
    run()