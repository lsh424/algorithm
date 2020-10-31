class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def find(i, j):
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            find(i - 1, j)
            find(i + 1, j)
            find(i, j - 1)
            find(i, j + 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] != '0':
                    find(r, c)
                    count += 1

        return count