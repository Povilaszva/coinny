from click.testing import CliRunner

from coinny import coinny


def test_coinny_ok():
    runner = CliRunner()
    result = runner.invoke(coinny, "--amount 34")
    assert result.output == "20 Coins x1\n10 Coins x1\n2 Coins x2\n"


def test_coinny_amount_exception():
    runner = CliRunner()
    result = runner.invoke(coinny, "--amount 0")
    assert result.exception
    assert 'Error: Invalid value for "--amount": ' \
           '0 is smaller than the minimum valid value 1.' in result.output


def test_coinny_custom_coin_set():
    runner = CliRunner()
    result = runner.invoke(coinny, "1 2 --amount 34")
    assert result.output == "2 Coins x17\n"


def test_coinny_no_answer():
    runner = CliRunner()
    result = runner.invoke(coinny, "2 4 --amount 3")
    assert result.output == "Cannot find the answer\n"
