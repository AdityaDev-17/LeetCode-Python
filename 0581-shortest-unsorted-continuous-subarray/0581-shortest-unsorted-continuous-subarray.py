class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        min_val = nums[left]
        max_val = nums[left]

        for i in range(left, right + 1):
            if nums[i] < min_val:
                min_val = nums[i]

            if nums[i] > max_val:
                max_val = nums[i]

        while left > 0 and nums[left - 1] > min_val:
            left -= 1

        while right < n - 1 and nums[right + 1] < max_val:
            right += 1

        return right - left + 1