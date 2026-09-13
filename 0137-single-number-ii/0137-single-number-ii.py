class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for bit in range(32):
            count = 0

            for num in nums:
                # Handle negative numbers using 32-bit representation
                if (num >> bit) & 1:
                    count += 1

            if count % 3 != 0:
                result |= (1 << bit)

        # Convert back to negative integer if needed
        if result >= 2**31:
            result -= 2**32

        return result