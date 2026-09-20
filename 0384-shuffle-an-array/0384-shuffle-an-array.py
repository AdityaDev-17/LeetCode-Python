import random

class Solution:

    def __init__(self, nums):
        self.original = nums[:]

    def reset(self):
        return self.original[:]

    def shuffle(self):
        nums = self.original[:]

        for i in range(len(nums) - 1, 0, -1):
            j = random.randint(0, i)

            nums[i], nums[j] = nums[j], nums[i]

        return nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()