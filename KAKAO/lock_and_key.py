import copy

def solution(key, lock):
    M = len(key)
    N = len(lock)

    def rotate(key):
        ret = [[0] * M for _ in range(M)]

        for r in range(M):
            for c in range(M):
                ret[c][M - 1 - r] = key[r][c]
        return ret

    def make_grid(lock):
        grid = [[0] * (M + (N - 1) * 2) for _ in range(N + (M - 1) * 2)]

        for r in range(N):
            for c in range(N):
                grid[M - 1 + r][M - 1 + c] = lock[r][c]
        return grid

    def is_unlocked(grid):
        for r in range(M - 1, M + N - 1):
            for c in range(M - 1, M + N - 1):
                if grid[r][c] != 1:
                    return False
        return True

    def translate(grid, key, row_step, col_step):
        for r in range(M):
            for c in range(M):
                grid[row_step + r][col_step + c] += key[r][c]
        return grid

    grid = make_grid(lock)
    key1 = rotate(key)
    key2 = rotate(key1)
    key3 = rotate(key2)

    for key in [key, key1, key2, key3]:
        for row_step in range(N + M - 1):
            for col_step in range(N + M - 1):
                g = translate(copy.deepcopy(grid), key, row_step, col_step)

                if is_unlocked(g):
                    return True

    return False