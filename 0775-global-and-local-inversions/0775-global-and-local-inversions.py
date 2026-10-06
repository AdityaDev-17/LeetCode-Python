class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        max_value = -1

        for i in range(len(nums) - 2):
            max_value = max(max_value, nums[i])

            if max_value > nums[i + 2]:
                return False

        return True