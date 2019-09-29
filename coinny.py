import click
from src.mincoins import make_change, count_frequency

STANDARD_COIN_VALUES = [1, 2, 5, 10, 20, 50]


@click.command()
@click.argument('coins', nargs=-1, type=click.IntRange(1))
@click.option('--amount', prompt='Change amount', help='The amount of change', type=click.IntRange(1))
def coinny(coins, amount):
    """coinny App, finding minimum amount of coins for a given change!

    STANDARD_COIN_VALUES = [1, 2, 5, 10, 20, 50],
    You can pass custom coin values. For example: "python coinny.py 1 2 6 13 21".
    """
    coins = STANDARD_COIN_VALUES if not coins else coins
    res = make_change(coins, amount)
    for key, value in count_frequency(res).items() if res else click.echo('Cannot find the answer'):
        click.echo(f"{key} Coins x{value}")


if __name__ == '__main__':  # pragma: no cover
    coinny()
