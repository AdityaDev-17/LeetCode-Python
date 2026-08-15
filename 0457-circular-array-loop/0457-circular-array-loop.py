class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):

            direction = nums[i] > 0

            slow = i
            fast = i

            while True:

                # Move slow once
                nxt = next_index(slow)
                if (nums[nxt] > 0) != direction:
                    break
                slow = nxt

                # Move fast once
                nxt = next_index(fast)
                if (nums[nxt] > 0) != direction:
                    break

                # Move fast second time
                nxt2 = next_index(nxt)
                if (nums[nxt2] > 0) != direction:
                    break

                fast = nxt2

                if slow == fast:

                    # Self-loop check
                    if slow == next_index(slow):
                        break

                    return True

        return False