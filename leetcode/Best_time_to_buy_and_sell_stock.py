class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        if not prices:
            return max_profit

        min_value = prices[0]

        for i in range(0, len(prices)):
            if prices[i] <= min_value:
                min_value = prices[i]

            if prices[i] - min_value > max_profit:
                max_profit = prices[i] - min_value

        return max_profit