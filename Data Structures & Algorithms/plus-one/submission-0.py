class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = 0
        start = 1
        for i in range(len(digits) - 1,-1,-1):
            x += digits[i] * start
            start *= 10

        x += 1

        result = []
        for val in str(x):
            result.append(int(val))

        return result