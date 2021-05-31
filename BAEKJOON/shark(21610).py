# 마법사 상어와 비바라기

n, m = map(int, input().split(' '))

g = []
pos = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
d_list = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
memo = [[0] * n for _ in range(n)]

for _ in range(n):
    g.append(list(map(int, list(input().split(' ')))))

for _ in range(m):
    d, s = map(int, input().split(' '))
    rd, rc = d_list[d - 1]
    for i in range(len(pos)):
        pos[i] = ((pos[i][0] + rd * s) % n, (pos[i][1] + rc * s) % n)
        g[pos[i][0]][pos[i][1]] += 1
        memo[pos[i][0]][pos[i][1]] = 1

    for p in pos:
        count = 0
        for r, c in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            rw, cw = p[0] + r, p[1] + c
            if 0 <= rw < n and 0 <= cw < n and g[rw][cw] > 0:
                count += 1
        g[p[0]][p[1]] += count

    pos = []
    for i in range(n):
        for j in range(n):
            if g[i][j] >= 2 and memo[i][j] == 0:
                g[i][j] -= 2
                pos.append((i, j))

            if memo[i][j] == 1:
                memo[i][j] = 0

answer = 0

for i in range(n):
    for j in range(n):
        answer += g[i][j]

print(answer)