class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        n = len(nums)

        # dp[i] = size of the largest divisible subset
        # ending at nums[i]
        dp = [1] * n

        # parent[i] = previous element in the subset
        parent = [-1] * n

        max_len = 1
        last = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                last = i

        # Reconstruct the subset
        result = []

        while last != -1:
            result.append(nums[last])
            last = parent[last]

        return result