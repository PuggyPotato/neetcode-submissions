class Solution:
    def maxScore(self, s: str) -> int:
        count_left = 0
        count_right = 0
        maximum = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                count_left += 1
            
            count_right = 0

            for j in range(i + 1,len(s)):
                if s[j] == "1":
                    count_right += 1

            maximum = max(maximum, count_left + count_right)

        return maximum
                 