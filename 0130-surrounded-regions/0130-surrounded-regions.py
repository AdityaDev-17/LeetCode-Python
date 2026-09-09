class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return

            if board[row][col] != 'O':
                return

            # Mark this O as safe
            board[row][col] = '#'

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Find O's on the top and bottom borders
        for col in range(n):
            dfs(0, col)
            dfs(m - 1, col)

        # Find O's on the left and right borders
        for row in range(m):
            dfs(row, 0)
            dfs(row, n - 1)

        # Capture surrounded O's
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'

                elif board[row][col] == '#':
                    board[row][col] = 'O'
        