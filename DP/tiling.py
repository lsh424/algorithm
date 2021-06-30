def solution(n):
    memo = [0] * 60000
    memo[1] = 1
    memo[2] = 2

    for i in range(3, n + 1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % 1000000007
    return memo[n]