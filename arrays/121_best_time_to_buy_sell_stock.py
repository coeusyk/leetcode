"""
----
Easy
----

You are given an array 'prices' where prices[i] is the price of a given stock on the 'ith' day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


def max_profit(prices: list[int]) -> int:
    max_pro = 0
    min_price = float("inf")

    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        max_pro = max(max_pro, prices[i] - min_price)

    return max_pro
