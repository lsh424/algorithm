class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        temp = 0
        satisfaction.sort()

        for i in range(1, len(satisfaction) + 1):
            temp += (i * satisfaction[i - 1])

        answer = temp

        for i in range(0, len(satisfaction)):
            temp = temp - sum(satisfaction[i:])

            if answer < temp:
                answer = temp

            if satisfaction[i] >= 0:
                break

        return answer