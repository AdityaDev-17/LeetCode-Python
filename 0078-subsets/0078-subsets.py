class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def backtrack(index):
            if index == len(nums):
                result.append(current[:])
                return

            # Include nums[index]
            current.append(nums[index])
            backtrack(index + 1)

            # Don't include nums[index]
            current.pop()
            backtrack(index + 1)

        backtrack(0)

        return result