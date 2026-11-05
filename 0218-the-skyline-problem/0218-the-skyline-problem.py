class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()

        result = []
        max_heap = [(0, float("inf"))]

        for x, neg_height, right in events:
            # Remove buildings that have ended
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)

            # Add a new building
            if neg_height:
                heapq.heappush(max_heap, (neg_height, right))

            current_height = -max_heap[0][0]

            # Add a key point only when height changes
            if not result or result[-1][1] != current_height:
                result.append([x, current_height])

        return result