class Solution:
    def canChange(self, start: str, target: str) -> bool:
        l = 0
        r = 0

        while l < len(start) and r < len(start):
            if start[l] == "_":
                l += 1
                continue
            if target[r] == "_":
                r += 1
                continue
            
            if start[l] != target[r]:
                return False
            elif target[r] == "R" and start[l] == "R" and r < l:
                return False
            elif target[r] == "L" and start[l] == "L" and l < r:
                return False
            else:
                l +=1 
                r += 1

        while l < len(start) and start[l] == "_":
            l += 1
        while r < len(target) and target[r] == "_":
            r += 1

        return True and l == r