from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        dic = defaultdict(int)
        answer = 0

        for c in s:
            dic[c] += 1
            end += 1

            if end - start == len(dic):
                answer = max(answer, end - start)
            elif end - start > len(dic):
                while len(dic) != end - start:
                    dic[s[start]] -= 1
                    if dic[s[start]] == 0:
                        del dic[s[start]]
                    start += 1

        return answer