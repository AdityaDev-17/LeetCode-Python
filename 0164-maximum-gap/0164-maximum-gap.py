class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        min_num = min(nums)
        max_num = max(nums)

        if min_num == max_num:
            return 0

        bucket_size = max(1, (max_num - min_num) // (n - 1))
        bucket_count = (max_num - min_num) // bucket_size + 1

        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count
        bucket_used = [False] * bucket_count

        for num in nums:
            index = (num - min_num) // bucket_size

            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)
            bucket_used[index] = True

        max_gap = 0
        previous_max = min_num

        for i in range(bucket_count):
            if not bucket_used[i]:
                continue

            max_gap = max(max_gap, bucket_min[i] - previous_max)
            previous_max = bucket_max[i]

        return max_gap