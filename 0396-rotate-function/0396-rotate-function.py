class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)

        total = sum(nums)

        current = 0
        for i in range(n):
            current += i * nums[i]

        maximum = current

        for k in range(1, n):
            current = current + total - n * nums[n - k]

            maximum = max(maximum, current)

        return maximum