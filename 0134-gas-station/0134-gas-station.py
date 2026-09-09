class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        current_gas = 0
        start = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]

            total_gas += gain
            current_gas += gain

            # Current starting point cannot reach station i + 1
            if current_gas < 0:
                start = i + 1
                current_gas = 0

        # Not enough gas overall
        if total_gas < 0:
            return -1

        return start