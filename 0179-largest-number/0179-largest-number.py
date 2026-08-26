class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        # Compare a+b with b+a
        # Example: "3" + "30" = "330"
        #          "30" + "3" = "303"
        # So "3" should come before "30"

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] + nums[i] > nums[i] + nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        result = ""

        for num in nums:
            result += num

        # Handle cases like [0, 0, 0]
        if result[0] == "0":
            return "0"

        return result