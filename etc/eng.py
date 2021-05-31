from collections import defaultdict

def solution(n, words):
    dic = defaultdict(int)

    for i in range(len(words)):
        if dic[words[i]] > 0 or (i > 0 and words[i - 1][-1] != words[i][0]):
            a, b = divmod(i, n)
            return [b + 1, a + 1]
        dic[words[i]] += 1

    return [0, 0]