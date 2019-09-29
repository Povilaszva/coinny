def make_change(coins: list, amount: int):
    """Function to find minimum amount of coins for a given change."""
    amount = amount
    result = [amount+1] * (amount+1)
    coins_used = [list()] * (amount+1)

    result[0] = 0
    for i in range(1, amount+1):
        for coin in [c for c in coins if i >= c]:
            if result[i - coin] + 1 < result[i]:
                result[i] = result[i-coin] + 1
                coins_used[i] = coins_used[i-coin] + [coin]
    return coins_used[amount]


def count_frequency(my_list):
    """Function to count frequency of matching coins."""
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
