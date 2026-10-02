class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        minutes = []

        for time in timePoints:
            hour = int(time[:2])
            minute = int(time[3:])
            
            minutes.append(hour * 60 + minute)

        minutes.sort()

        min_diff = 1440

        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        # Difference between last and first across midnight
        min_diff = min(min_diff, 1440 - minutes[-1] + minutes[0])

        return min_diff