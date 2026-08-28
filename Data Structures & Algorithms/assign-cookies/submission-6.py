class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ptr = 0
        g.sort()
        s.sort()

        for i in range(len(s)):
            if ptr < len(g) and s[i] >= g[ptr]:
                ptr += 1

        return ptr