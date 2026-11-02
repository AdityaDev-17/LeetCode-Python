class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []

        def backtrack(start, current, total):

            if len(current) == k:
                if total == n:
                    result.append(current.copy())
                return

            for i in range(start, 10):

                if total + i > n:
                    break

                current.append(i)

                backtrack(i + 1, current, total + i)

                current.pop()

        backtrack(1, [], 0)

        return result