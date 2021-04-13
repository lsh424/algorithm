import sys
sys.setrecursionlimit(10**7)
memo = [0] * 100001
memo[0] = 0
memo[1] = 1

def solution(n):
    if n == 0 or memo[n] != 0:
        return memo[n]
    else:
        memo[n] = solution(n-1) + solution(n-2)
        return memo[n] % 1234567