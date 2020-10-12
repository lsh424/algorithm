import collections

def solution(clothes):
    answer = 1
    dict = collections.defaultdict(list)

    for c in clothes:
        dict[c[-1]].append(c[0])

    for value in dict.values():
        answer *= len(value) + 1

    return answer - 1