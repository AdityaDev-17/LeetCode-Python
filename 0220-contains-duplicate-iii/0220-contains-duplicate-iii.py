class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False

        bucket_size = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):
            bucket_id = num // bucket_size

            # Check the same bucket
            if bucket_id in buckets:
                return True

            # Check adjacent buckets
            if bucket_id - 1 in buckets:
                if abs(num - buckets[bucket_id - 1]) <= valueDiff:
                    return True

            if bucket_id + 1 in buckets:
                if abs(num - buckets[bucket_id + 1]) <= valueDiff:
                    return True

            buckets[bucket_id] = num

            # Maintain the sliding window
            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket]

        return False