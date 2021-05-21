import heapq

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
q = []

for y in range(n):
    for x in range(n):
        if g[y][x] == 9:
            heapq.heappush(q, (0, y, x))
            g[y][x] = 0

size, eat = 2, 0
answer = 0
visit = []

while q:
    d, y, x = heapq.heappop(q)
    if 0 < g[y][x] < size:
        eat += 1
        g[y][x] = 0
        if eat == size:
            size += 1
            eat = 0

        answer += d
        d = 0
        q = []
        visit = []

    for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
        nd, ny, nx = d + 1, y + dy, x + dx
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if 0 < g[ny][nx] > size or [ny, nx] in visit:
            continue

        visit.append([ny, nx])
        heapq.heappush(q, [nd, ny, nx])

print(answer)