class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        amount = 0
        for value in counter.values():
            while value > 1:
                amount += 2
                value -= 2

        for value in counter.values():
            if value != 0 and value % 2 != 0:
                amount += 1
                break


        return amount