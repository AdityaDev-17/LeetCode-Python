class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0

        for bit in range(30):
            ones = 0

            for num in nums:
                if (num >> bit) & 1:
                    ones += 1

            zeros = n - ones

            total += ones * zeros

        return total