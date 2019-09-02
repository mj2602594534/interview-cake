def get_max_profit_2(prices):
    """Returns the maximum profit

    >>> get_max_profit_2([10, 7, 5, 8, 11, 9])
    6

    """

    # start with the first price available for purchase
    buy_price = prices[0]

    # find the max profit from the first buy (O(n))
    max_profit = max([prices[i] - buy_price for i in range(1,len(prices))])

    # go through prices and repeat above process, if price < buy_price
    for idx, price in enumerate(prices[1:]):
        if price < buy_price:
            max_profit = max(prices[idx:]) - price
            buy_price = price

    return max_profit

get_max_profit_2([10, 7, 5, 8, 11, 9])