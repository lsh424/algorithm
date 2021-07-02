from collections import deque

def can_move(cur1, cur2, new_board):
    cand = []

    # 평행 이동
    for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        next1 = (cur1[0] + dy, cur1[1] + dx)
        next2 = (cur2[0] + dy, cur2[1] + dx)

        if new_board[next1[0]][next1[1]] == 0 and new_board[next2[0]][next2[1]] == 0:
            cand.append((next1, next2))

    # 회전

    # 가로방향
    if cur1[0] == cur2[0]:
        for d in [-1, 1]:
            if new_board[cur1[0] + d][cur1[1]] == 0 and new_board[cur2[0] + d][cur2[1]] == 0:
                cand.append((cur1, (cur1[0] + d, cur1[1])))
                cand.append((cur2, (cur2[0] + d, cur2[1])))
    # 세로방향
    else:
        for d in [-1, 1]:
            if new_board[cur1[0]][cur1[1] + d] == 0 and new_board[cur2[0]][cur2[1] + d] == 0:
                cand.append(((cur1[0], cur1[1] + d), cur1))
                cand.append(((cur2[0], cur2[1] + d), cur2))

    return cand

def solution(board):
    N = len(board)
    new_board = [[1] * (N + 2) for _ in range(N + 2)]

    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque([((1, 1), (1, 2), 0)])
    check = set([((1, 1), (1, 2))])

    while q:
        cur1, cur2, count = q.popleft()

        if cur1 == (N, N) or cur2 == (N, N):
            return count

        for nxt in can_move(cur1, cur2, new_board):
            if nxt not in check:
                q.append((nxt[0], nxt[1], count + 1))
                check.add(nxt)