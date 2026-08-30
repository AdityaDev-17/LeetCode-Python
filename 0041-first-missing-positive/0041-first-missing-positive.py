class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0

        while i < n:
            # Place nums[i] at index nums[i] - 1
            # if the value is in the valid range [1, n]
            # and is not already in its correct position.
            if 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        # Find the first index where the number is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # All numbers 1..n are present
        return n + 1