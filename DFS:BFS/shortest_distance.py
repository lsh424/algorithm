from collections import deque

def solution(maps):
    q = deque([(0, 0)])

    while q:
        r, c = q.popleft()
        for (dr, dc) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_r, next_c = r + dr, c + dc
            if 0 <= next_r < len(maps) and 0 <= next_c < len(maps[0]):
                if maps[next_r][next_c] == 1:
                    maps[next_r][next_c] = (maps[r][c] + 1)
                    q.append((next_r, next_c))

    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]