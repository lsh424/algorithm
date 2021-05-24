# 적록색약
from collections import deque

n = int(input())
g = []
another_g = []

for _ in range(n):
    s = input()
    g.append(list(s))
    another_g.append(list(s.replace('G','R')))

def sol(g, RGB_count, visit):
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                color = g[i][j]
                RGB_count[color] += 1
                q = deque([(i,j)])
                while q:
                    x,y = q.popleft()

                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nx = x + dx
                        ny = y + dy
                        if nx >= 0 and nx < n and ny >= 0 and ny < n:
                            if g[nx][ny] == color:
                                g[nx][ny] = 'X'
                                q.append((nx,ny))
                                visit[nx][ny] = 1

    return RGB_count["R"] + RGB_count["G"] + RGB_count["B"]

print(sol(g, {"R": 0, "G": 0, "B": 0}, [([0] * n) for _ in range(n)]), sol(another_g, {"R": 0, "G": 0, "B": 0}, [([0] * n) for _ in range(n)]))