class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return

            if grid[row][col] != "1":
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)

        return count