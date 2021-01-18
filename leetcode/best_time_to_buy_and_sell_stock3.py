# 어려워서 다른사람 풀이 확인 ㅜ

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        one_buy = two_buy = sys.maxsize
        one_profit = two_profit = 0
        for p in prices:
            one_buy = min(one_buy, p)
            one_profit = max(one_profit, p - one_buy)
            two_buy = min(two_buy, p - one_profit)
            two_profit = max(two_profit, p - two_buy)
        return two_profit


