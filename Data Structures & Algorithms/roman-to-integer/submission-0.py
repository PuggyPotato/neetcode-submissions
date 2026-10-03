class Solution:
    def romanToInt(self, s: str) -> int:
        ptr = 0
        count = 0

        while ptr < len(s):
            if s[ptr] == "I":
                if ptr + 1 < len(s) and s[ptr + 1] == "V":
                    count += 4
                    ptr += 1
                elif ptr + 1 < len(s) and s[ptr + 1] == "X":
                    count += 9
                    ptr += 1
                else:
                    count += 1

            elif s[ptr] == "X":
                if ptr + 1 < len(s) and s[ptr + 1] == "L":
                    count += 40
                    ptr += 1
                elif ptr + 1 < len(s) and s[ptr + 1] == "C":
                    count += 90
                    ptr += 1    
                else:
                    count += 10

            elif s[ptr] == "C":
                if ptr + 1 < len(s) and s[ptr + 1] == "D":
                    count += 400
                    ptr += 1
                elif ptr + 1 < len(s) and s[ptr + 1] == "M":
                    count += 900
                    ptr += 1       
                else:
                    count += 100

            elif s[ptr] == "V":
                count += 5

            elif s[ptr] == "L":
                count += 50

            elif s[ptr] == "D":
                count += 500

            elif s[ptr] == "M":
                count += 1000

            ptr += 1

        return count               
                