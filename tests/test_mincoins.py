from src.mincoins import make_change, count_frequency


def test_make_change_standard_coins(standard_coin_set):
    res = make_change(standard_coin_set, 63)
    assert res == [50, 10, 2, 1]


def test_make_change_zero(standard_coin_set):
    res = make_change(standard_coin_set, 0)
    assert res == []


def test_make_change_custom_coins(custom_coin_set):
    res = make_change(custom_coin_set, 66)
    assert res == [22, 22, 22]


def test_make_change_custom_even_coins(custom_coin_set_even):
    res = make_change(custom_coin_set_even, 11)
    assert res == []


def test_count_frequency(list_of_coins):
    res = count_frequency(list_of_coins)
    assert res == {3: 1, 4: 2, 5: 1, 6: 1, 7: 5, 99: 1}
