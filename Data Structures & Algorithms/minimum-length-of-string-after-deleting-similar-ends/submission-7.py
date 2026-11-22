class Solution:
    def minimumLength(self, s: str) -> int:
        s = list(s)
        l = 0
        r = len(s) - 1

        if len(s) == 1:
            return 1

        while True:
            if l <= r and s[l] == s[r] and l != r:
                temp = s[l]
                while l <= r and s[l] == temp:
                    l += 1
                while l <= r and s[r] == temp:
                    r -= 1
            else:
                break

        return max(r-l+1, 0)