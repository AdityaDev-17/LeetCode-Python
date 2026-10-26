from typing import List
from itertools import combinations
from math import prod

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        if prod(nums) != target * target:
            return False

        for size in range(1, n):
            for subset in combinations(nums, size):
                if prod(subset) == target:
                    return True

        return False