class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        l = 0
        r = 0
        for i in range(len(s)):

            if i == len(s) - 1 or s[i] == " ":
                if s[i] == " ":
                    r = i - 1
                else:
                    r = i
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                l = i + 1

        return "".join(s)