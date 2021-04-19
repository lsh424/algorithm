def solution(stones, k):
    left = 1
    right = max(stones[:k])
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        is_pass = True
        count = 0

        for i in stones:
            if i - mid < 0:
                count += 1
            else:
                count = 0

            if count >= k:
                is_pass = False
                break

        if is_pass == True:
            if mid > answer:
                answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer