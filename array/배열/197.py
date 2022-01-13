import sys


def stockTrade(n: list[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in n:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)
    return profit


stock = [7,1,5,3,6,4]
print(stockTrade(stock))