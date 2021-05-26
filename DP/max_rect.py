# dp

def solution(board):
    h = len(board)
    w = len(board[0])

    for i in range(1, h):
        for j in range(1, w):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1

    return max([j for i in board for j in i]) ** 2