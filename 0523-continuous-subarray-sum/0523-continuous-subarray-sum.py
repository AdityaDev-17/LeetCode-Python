class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder_index = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            remainder = total % k

            if remainder in remainder_index:
                if i - remainder_index[remainder] >= 2:
                    return True
            else:
                remainder_index[remainder] = i

        return False