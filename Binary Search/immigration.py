def solution(n, times):
    t = min(times)
    ls = list(filter(lambda x: x < n * t, times))

    left = t
    right = n * t
    answer = n * t

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for i in ls:
            total += (mid // i)

        if total < n:
            left = mid + 1
        else:
            right = mid - 1
            if answer > mid:
                answer = mid
    return answer