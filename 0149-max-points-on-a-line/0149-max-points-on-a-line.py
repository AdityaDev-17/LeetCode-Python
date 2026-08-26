class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n

        result = 0

        for i in range(n):
            slopes = {}

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                # Vertical line
                if dx == 0:
                    slope = (1, 0)

                # Horizontal line
                elif dy == 0:
                    slope = (0, 1)

                else:
                    # Reduce slope to its simplest form
                    from math import gcd

                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g

                    # Keep the sign consistent
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dy, dx)

                slopes[slope] = slopes.get(slope, 0) + 1

                result = max(result, slopes[slope] + 1)

        return result