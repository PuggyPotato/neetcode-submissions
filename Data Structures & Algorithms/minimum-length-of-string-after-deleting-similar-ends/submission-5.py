class Solution:
    def minimumLength(self, s: str) -> int:
        s = list(s)
        while True:
            if len(s) > 1 and s[0] == s[-1]:
                temp = s[0]
                while len(s) > 0 and s[0] == temp:
                    s.pop(0)
                while len(s) > 0 and s[-1] == temp:
                    s.pop()
            else:
                break
        return len(s)