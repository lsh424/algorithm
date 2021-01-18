class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices[0]
        profit = 0

        for p in prices:
            if p > price:
                profit += (p - price)
            price = p

        return profit