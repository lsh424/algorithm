def solution(n):
    answer = 1
    if n == 1:
        return 1
    else:
        while n != 1:
            n , r = divmod(n,2)
            if r == 1:
                answer += 1
    return answer