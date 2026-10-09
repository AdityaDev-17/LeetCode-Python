class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows - 2):
            for c in range(cols - 2):
                nums = set()

                for i in range(3):
                    for j in range(3):
                        nums.add(grid[r + i][c + j])

                if nums != set(range(1, 10)):
                    continue

                if grid[r + 1][c + 1] != 5:
                    continue

                valid = True

                for i in range(3):
                    if sum(grid[r + i][c:c + 3]) != 15:
                        valid = False

                    if sum(grid[r][c + i] for r in range(r, r + 3)) != 15:
                        valid = False

                if sum(grid[r + i][c + i] for i in range(3)) != 15:
                    valid = False

                if sum(grid[r + i][c + 2 - i] for i in range(3)) != 15:
                    valid = False

                if valid:
                    count += 1

        return count