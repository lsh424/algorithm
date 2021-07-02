n = int(input())
dp = [0] * 30
schedule = [0] * n

for i in range(n):
    schedule[i] = tuple(map(int, input().split(' ')))

for i in range(n):
    if dp[i] > dp[i + 1]:
        dp[i + 1] = dp[i]
    if dp[i + schedule[i][0]] < dp[i] + schedule[i][1]:
        dp[i + schedule[i][0]] = dp[i] + schedule[i][1]

print(dp[n])