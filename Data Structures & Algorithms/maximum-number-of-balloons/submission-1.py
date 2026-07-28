class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = [0] * 26
        for char in text:
            freq[ord(char) - ord('a')] += 1

        count = 0
        
        while freq[0] > 0 and freq[1] > 0 and freq[11] > 1 and freq[14] > 1 and freq[13] > 0:
            freq[0] -= 1
            freq[1] -= 1
            freq[11] -= 2
            freq[14] -= 2
            freq[13] -= 1
            count += 1
        
        return count


# b = 1
# a = 0
# l = 11
# o = 14
# n = 13