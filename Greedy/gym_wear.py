def solution(n, lost, reserve):
    rsv = list(set(reserve) - set(lost))
    lost = list(set(lost) - set(reserve))

    lost.sort()

    for i in lost:
        if i - 1 in rsv:
            rsv.remove(i - 1)
        elif i + 1 in rsv:
            rsv.remove(i + 1)
        else:
            n -= 1

    answer = n
    return answer