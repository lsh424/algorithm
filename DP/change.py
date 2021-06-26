# 어려움
def solution(n, money):
    memo = [1] + [0] * n

    for m in money:
        for price in range(m, n + 1):
            if price >= m:
                memo[price] += memo[price - m]
    return memo[n] % 1000000007