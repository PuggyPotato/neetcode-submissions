class Solution:
    def maxScore(self, s: str) -> int:
        zero_left = 0
        one_right = s.count("1")
        maximum = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                zero_left += 1
            else:
                one_right -= 1

            maximum = max(maximum, zero_left + one_right)

        return maximum