def solution(progresses, speeds):
    length = len(progresses)
    index = 0
    v = 0
    answer = []

    while index < length:
        for i in range(index, length):
            progresses[i] += speeds[i]

            if progresses[index] >= 100:
                index += 1
                v += 1
        if v >= 1:
            answer.append(v)
            v = 0

    return answer