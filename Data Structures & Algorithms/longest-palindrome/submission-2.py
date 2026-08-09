class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        amount = 0
        has_odd = False
        for value in counter.values():
            amount += (value // 2) * 2

            if value % 2 == 1:
                has_odd = True

        if has_odd:
            return amount + 1

        return amount