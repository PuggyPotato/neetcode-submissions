class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        freq = [0] * 1001

        for val in skill:
            freq[val] += 1

        l = 0
        r = len(freq) - 1

        total = 0
        benchmark = 0

        while l <= r:

            if freq[l] == 0:
                l += 1
                continue

            if freq[r] == 0:
                r -= 1
                continue

            if total == 0:
                benchmark = l + r
                total += l * r
            elif l + r != benchmark:
                return -1
            else:
                total += l * r
            
            freq[l] -= 1
            freq[r] -= 1
            
            

        return total
            

            
            