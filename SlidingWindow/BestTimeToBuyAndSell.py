from typing import List

def maxProfit(prices: List[int]) -> int: 
    minPrice = prices[0]
    maxProfit = 0

    for price in prices: 
        if price < minPrice: 
            minPrice = price 
        profit = price - minPrice
        maxProfit = max(maxProfit, profit)

    return maxProfit 

prices = [7, 1, 5, 6, 4, 3, 2]
print(maxProfit(prices))