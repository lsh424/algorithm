def solution(n, k):
    answer = []
    numList = [i for i in range(1, n + 1)]
    memo = [0] * (n + 1)
    memo[0] = 1
    memo[1] = 1

    def factorial(n):
        if memo[n] != 0:
            return memo[n]
        else:
            memo[n] = n * factorial(n - 1)
            return memo[n]

    while n != 0:
        idx, k = divmod(k, factorial(n - 1))
        if k == 0:
            answer.append(numList.pop(idx - 1))
        else:
            answer.append(numList.pop(idx))
        n -= 1
    return answer