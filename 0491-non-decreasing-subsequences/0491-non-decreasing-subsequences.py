class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        result = []
        current = []

        def backtrack(start):
            if len(current) >= 2:
                result.append(current[:])

            used = set()

            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue

                if current and nums[i] < current[-1]:
                    continue

                used.add(nums[i])
                current.append(nums[i])

                backtrack(i + 1)

                current.pop()

        backtrack(0)
        return result