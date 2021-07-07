import math

n = int(input())
pos = [n // 2, n // 2]  # e, w, s, n
direction = 'w'
board = []

answer = 0
check = [[0] * n for _ in range(n)]
w = [(-1, -1, 0.1), (-1, 0, 0.07), (-2, 0, 0.02), (-1, 1, 0.01), (0, -2, 0.05), (1, -1, 0.1), (1, 0, 0.07),
     (1, 1, 0.01), (2, 0, 0.02), (0, -1, 'a')]

for _ in range(n):
    board.append(list(map(int, input().split(' '))))

for i in range(n ** 2):
    if pos == [0, 0]:
        break

    check[pos[0]][pos[1]] = 1
    if direction == 'w':
        pos[1] -= 1
        remain = board[pos[0]][pos[1]]
        for (dr, dc, p) in w:
            sand = 0
            if p == 'a':
                sand = remain
            else:
                sand = math.trunc(board[pos[0]][pos[1]] * p)
                remain -= sand
            nr, nc = pos[0] + dr, pos[1] + dc
            if 0 <= nr <= n - 1 and 0 <= nc <= n - 1:
                board[nr][nc] += sand
            else:
                answer += sand
        if check[pos[0] + 1][pos[1]] == 0 or pos[1] == 0:
            direction = 's'
    elif direction == 's':
        pos[0] += 1
        remain = board[pos[0]][pos[1]]
        for (dr, dc, p) in w:
            sand = 0
            if p == 'a':
                sand = remain
            else:
                sand = math.trunc(board[pos[0]][pos[1]] * p)
                remain -= sand
            nr, nc = pos[0] + (dc * -1), pos[1] + dr
            if 0 <= nr <= n - 1 and 0 <= nc <= n - 1:
                board[nr][nc] += sand
            else:
                answer += sand
        if check[pos[0]][pos[1] + 1] == 0 or pos[0] == n - 1:
            direction = 'e'
    elif direction == 'e':
        pos[1] += 1
        remain = board[pos[0]][pos[1]]
        for (dr, dc, p) in w:
            sand = 0
            if p == 'a':
                sand = remain
            else:
                sand = math.trunc(board[pos[0]][pos[1]] * p)
                remain -= sand
            nr, nc = pos[0] + dr, pos[1] + (dc * -1)
            if 0 <= nr <= n - 1 and 0 <= nc <= n - 1:
                board[nr][nc] += sand
            else:
                answer += sand
        if check[pos[0] - 1][pos[1]] == 0 or pos[1] == n - 1:
            direction = 'n'
    else:
        pos[0] -= 1
        remain = board[pos[0]][pos[1]]
        for (dr, dc, p) in w:
            sand = 0
            if p == 'a':
                sand = remain
            else:
                sand = math.trunc(board[pos[0]][pos[1]] * p)
                remain -= sand
            nr, nc = pos[0] + dc, pos[1] + (dr * -1)
            if 0 <= nr <= n - 1 and 0 <= nc <= n - 1:
                board[nr][nc] += sand
            else:
                answer += sand
        if check[pos[0]][pos[1] - 1] == 0 or pos[0] == 0:
            direction = 'w'
            
print(answer)