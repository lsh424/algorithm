# 로봇 청소기
from collections import deque

n, m = map(int, (input().split(' ')))
x, y, d = map(int, (input().split(' ')))

g = []
direction = [0, 1, 2, 3]
answer = 0
dic = {0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)}

for _ in range(n):
    g.append(list(map(int, input().split(' '))))

q = deque([(x, y, d)])

while q:
    x, y, d = q.popleft()
    if g[x][y] == 0:
        answer += 1
    g[x][y] = -1
    x_pos = x
    y_pos = y
    origin_d = d
    count = 0

    while g[x_pos][y_pos] != 0 and count < 4:
        x_pos, y_pos = x + dic[d][0], y + dic[d][1]
        d = direction[d - 1]
        count += 1

    if origin_d == d and g[x_pos][y_pos] != 0:
        if d == 0:
            x, y = x + 1, y
        elif d == 1:
            x, y = x, y - 1
        elif d == 2:
            x, y = x - 1, y
        else:
            x, y = x, y + 1

        if g[x][y] == 1:
            break
        else:
            q.append((x, y, d))
    else:
        q.append((x_pos, y_pos, d))

print(answer)