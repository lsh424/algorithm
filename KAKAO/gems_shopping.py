from collections import defaultdict

def solution(gems):
    kind = len(set(gems))
    length = len(gems)
    answer = [0, length]
    start, end = 0, 0
    dic = defaultdict(int)
    dic[gems[end]] += 1

    while True:
        if len(dic) == kind:
            if end - start < answer[1] - answer[0]:
                answer[0] = start + 1
                answer[1] = end + 1
            dic[gems[start]] -= 1
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start += 1
        else:
            end += 1
            if end == len(gems):
                return answer
            dic[gems[end]] += 1