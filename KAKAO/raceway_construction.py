def solution(board):
    n = len(board)
    cost = [[float('Inf')] * n for _ in range(n)]
    cost[0][0] = 0

    # direction = s(시작), r(행으로 이동), c(열로 이동)
    def build(i, j, direction):
        if j + 1 < n and board[i][j + 1] == 0:
            if direction == 's' or direction == 'r':
                if cost[i][j + 1] >= cost[i][j] + 100:
                    cost[i][j + 1] = cost[i][j] + 100
                    build(i, j + 1, 'r')
            else:
                if cost[i][j + 1] >= cost[i][j] + 600:
                    cost[i][j + 1] = cost[i][j] + 600
                    build(i, j + 1, 'r')

        if j - 1 >= 0 and board[i][j - 1] == 0:
            if direction == 'r':
                if cost[i][j - 1] >= cost[i][j] + 100:
                    cost[i][j - 1] = cost[i][j] + 100
                    build(i, j - 1, 'r')
            else:
                if cost[i][j - 1] >= cost[i][j] + 600:
                    cost[i][j - 1] = cost[i][j] + 600
                    build(i, j - 1, 'r')

        if i + 1 < n and board[i + 1][j] == 0:
            if direction == 's' or direction == 'c':
                if cost[i + 1][j] >= cost[i][j] + 100:
                    cost[i + 1][j] = cost[i][j] + 100
                    build(i + 1, j, 'c')
            else:
                if cost[i + 1][j] >= cost[i][j] + 600:
                    cost[i + 1][j] = cost[i][j] + 600
                    build(i + 1, j, 'c')

        if i - 1 >= 0 and board[i - 1][j] == 0:
            if direction == 'c':
                if cost[i - 1][j] >= cost[i][j] + 100:
                    cost[i - 1][j] = cost[i][j] + 100
                    build(i - 1, j, 'c')
            else:
                if cost[i - 1][j] >= cost[i][j] + 600:
                    cost[i - 1][j] = cost[i][j] + 600
                    build(i - 1, j, 'c')

    build(0, 0, 's')
    return cost[n - 1][n - 1]