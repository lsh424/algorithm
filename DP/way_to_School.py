from collections import deque

def solution(m, n, puddles):
    g = [[0] * m for _ in range(n)]
    q = deque([(0, 0)])
    g[0][0] = 1

    for p in puddles:
        g[p[1] - 1][p[0] - 1] = -1

    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (1, 0)]:
            next_r = r + dr
            next_c = c + dc
            if next_r < n and next_c < m and g[next_r][next_c] != -1:
                if g[next_r][next_c] == 0:
                    q.append((next_r, next_c))

                if g[next_r][next_c] == 0:
                    if next_r > 0:
                        g[next_r][next_c] += max(0, g[next_r - 1][next_c])
                    if next_c > 0:
                        g[next_r][next_c] += max(0, g[next_r][next_c - 1])

    return g[n - 1][m - 1] % 1000000007