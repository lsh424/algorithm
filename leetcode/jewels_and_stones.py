from collections import defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic = defaultdict(int)
        answer = 0

        for stone in stones:
            dic[stone] += 1

        for jewel in jewels:
            answer += dic[jewel]

        return answer