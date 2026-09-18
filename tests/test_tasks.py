import pytest

from tasks import (
    distance, circle, operations, favorite_movies,
    my_family, zoo, songs_list, secret,
    garden, shopping, store,
)


def test_distance():
    sites = {'A': (0, 0), 'B': (3, 4)}
    res = distance.calc_distances(sites)
    assert res['A']['B'] == pytest.approx(5.0)
    assert 'A' not in res['A']


def test_circle_area():
    assert circle.circle_area(1) == pytest.approx(3.1416, abs=0.001)


def test_is_inside_true():
    assert circle.is_inside_circle((0, 0), 10) is True


def test_is_inside_false():
    assert circle.is_inside_circle((100, 100), 10) is False


def test_operations():
    assert operations.get_25() == 25


def test_favorite_movies():
    first, last, second, second_last = favorite_movies.get_movies(
        favorite_movies.my_favorite_movies
    )
    assert first == 'Терминатор'
    assert last == 'Назад в будущее'
    assert second == 'Пятый элемент'
    assert second_last == 'Чужие'


def test_my_family():
    fam = [['я', 180], ['мама', 170], ['папа', 172]]
    assert my_family.get_father_height(fam) == 172
    assert my_family.get_total_height(fam) == 522


def test_zoo():
    zoo_list = zoo.build_zoo(
        ['lion', 'kangaroo', 'elephant', 'monkey'],
        ['rooster', 'ostrich', 'lark'],
    )
    assert 'bear' in zoo_list
    assert 'elephant' not in zoo_list
    assert zoo.get_cell(zoo_list, 'lion') == 1


def test_songs_list():
    songs = [['Halo', 4.9], ['Enjoy the Silence', 4.2], ['Clean', 5.83]]
    assert songs_list.songs_time_from_list(
        songs, ['Halo', 'Enjoy the Silence', 'Clean']
    ) == pytest.approx(14.93, abs=0.001)


def test_songs_dict():
    songs = {'Halo': 4.30, 'Enjoy the Silence': 4.6, 'Clean': 5.68}
    assert songs_list.songs_time_from_dict(
        songs, ['Halo', 'Enjoy the Silence', 'Clean']
    ) == pytest.approx(14.58, abs=0.001)


def test_secret():
    assert secret.decrypt(secret.secret_message) == 'в бане веник дороже денег'


def test_garden():
    g = ('ромашка', 'роза', 'одуванчик')
    m = ('ромашка', 'клевер')
    _, common, only_g, only_m = garden.flowers_analysis(g, m)
    assert common == {'ромашка'}
    assert only_g == {'роза', 'одуванчик'}
    assert only_m == {'клевер'}


def test_shopping():
    s = shopping.build_sweets()
    assert 'печенье' in s
    assert len(s['печенье']) == 2
    assert s['печенье'][0]['price'] <= s['печенье'][1]['price']


def test_store():
    goods = {'Лампа': '12345'}
    st = {'12345': [{'quantity': 27, 'price': 42}]}
    res = store.calc_goods_stats(goods, st)
    assert res[0]['name'] == 'Лампа'
    assert res[0]['quantity'] == 27
    assert res[0]['cost'] == 1134