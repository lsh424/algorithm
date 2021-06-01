# 주사위 굴리기
n, m, x, y, k = map(int, input().split(' '))

g = []

for _ in range(n):
    g.append(list(map(int, input().split(' '))))

# 동쪽 1, 서쪽 2, 북쪽 3, 남쪽 4
d = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
dsnb = [3, 4, 5, 2]  # 동서남북
dice_value = [0, 0, 0, 0, 0, 0]
bottom = 1
top = 6

for i in map(int, input().split(' ')):
    if 0 <= x + d[i][0] < n and 0 <= y + d[i][1] < m:
        b = bottom
        t = top

        if i == 1:
            bottom = dsnb[0]
            top = dsnb[1]
            dsnb[1] = b
            dsnb[0] = t
        elif i == 2:
            bottom = dsnb[1]
            top = dsnb[0]
            dsnb[1] = t
            dsnb[0] = b
        elif i == 3:
            bottom = dsnb[3]
            top = dsnb[2]
            dsnb[3] = t
            dsnb[2] = b
        elif i == 4:
            bottom = dsnb[2]
            top = dsnb[3]
            dsnb[3] = b
            dsnb[2] = t

        x += d[i][0]
        y += d[i][1]

        if g[x][y] == 0:
            g[x][y] = dice_value[bottom - 1]
        else:
            dice_value[bottom - 1] = g[x][y]
            g[x][y] = 0

        print(dice_value[top - 1])