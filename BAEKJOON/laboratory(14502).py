import itertools
from collections import deque
import copy

row, column = map(int, input().split(' '))
g = []
blanks = []
virus = []
answer = 0

def find_safe_area(candidate, g) -> int:
    global row, column
    safe_area = 0

    for c in candidate:
        g[c[0]][c[1]] = 1

    for v in virus:
        q = deque([v])
        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = x + dx
                ny = y + dy

                if nx >= 0 and nx < row and ny >= 0 and ny < column:
                    if g[nx][ny] == 0:
                        g[nx][ny] = 2
                        q.append((nx, ny))

    for r in g:
        safe_area += r.count(0)

    return safe_area


for i in range(row):
    ls = list(map(int, input().split(' ')))
    for j in range(column):
        if ls[j] == 0:
            blanks.append((i, j))
        elif ls[j] == 2:
            virus.append((i, j))

    g.append(ls)

for candidate in itertools.combinations(blanks, 3):
    m = copy.deepcopy(g)
    answer = max(answer, find_safe_area(candidate, m))

print(answer)