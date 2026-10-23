class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        count = [0] * len(timePoints)

        for i, val in enumerate(timePoints):
            time = int(val[0]) * 10 * 60 + int(val[1]) * 60 + int(val[-1]) + int(val[-2]) * 10
            count[i] = time

        count.sort()

        minimum = 9999

        for i in range(len(count) -1, -2, -1):

            if i == 0:
                minimum = min(minimum, count[i] + 1440 - count[i - 1])
            else:
                minimum = min(minimum, abs(count[i] - count[i - 1]))

        return minimum
        
