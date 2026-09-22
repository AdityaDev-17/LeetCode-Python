class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        count = 0

        for i in range(len(points)):
            distances = {}

            for j in range(len(points)):
                if i == j:
                    continue

                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]

                distance = dx * dx + dy * dy

                if distance in distances:
                    distances[distance] += 1
                else:
                    distances[distance] = 1

            for frequency in distances.values():
                count += frequency * (frequency - 1)

        return count