from collections import deque

row, col = map(int, input().split(' '))

queue = deque([(0, 0)])
graph = []

for _ in range(row):
    graph.append(list(input()))

visit = [[0] * col for _ in range(row)]
visit[0][0] = 1

while queue:
    i, j = queue.popleft()

    if (i, j) == (row - 1, col - 1):
        print(visit[i][j])
        break

    if i - 1 >= 0 and graph[i - 1][j] == '1' and visit[i - 1][j] == 0:
        queue.append((i - 1, j))
        visit[i - 1][j] = visit[i][j] + 1

    if i + 1 < row and graph[i + 1][j] == '1' and visit[i + 1][j] == 0:
        queue.append((i + 1, j))
        visit[i + 1][j] = visit[i][j] + 1

    if j - 1 >= 0 and graph[i][j - 1] == '1' and visit[i][j - 1] == 0:
        queue.append((i, j - 1))
        visit[i][j - 1] = visit[i][j] + 1

    if j + 1 < col and graph[i][j + 1] == '1' and visit[i][j + 1] == 0:
        queue.append((i, j + 1))
        visit[i][j + 1] = visit[i][j] + 1