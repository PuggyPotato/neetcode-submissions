class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        val = [0] * len(s)
        s = list(s)
        count = 0
        for shift in shifts:
            change = 1 if shift[2] == 1 else -1
            val[shift[0]] += change
            if shift[1] + 1 < len(s):
                val[shift[1] + 1] -= change

        for i in range(len(val)):
            count += val[i]
            s[i] = chr((ord(s[i]) - ord('a') + count) % 26 + ord('a')) 
        
        print(val)
        return "".join(s)

