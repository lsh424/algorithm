import collections

r, c = map(int, input().split(' '))
board = []
memo = [[""] * c for _ in range(r)]

for _ in range(r):
    board.append(list(input()))

q = collections.deque([(0, 0, board[0][0])])
answer = 0

while q:
    y, x, s = q.popleft()
    answer = max(answer, len(s))

    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_y, next_x = y + dy, x + dx
        if 0 <= next_y < r and 0 <= next_x < c:
            if board[next_y][next_x] not in s and memo[next_y][next_x] != s + board[next_y][next_x]:
                memo[next_y][next_x] = s + board[next_y][next_x]
                q.append((next_y, next_x, s + board[next_y][next_x]))

print(answer)