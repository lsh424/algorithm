def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    length = len(citations)

    for i in range(0, length):
        if answer >= citations[i]:
            return answer
        answer += 1
    return answer