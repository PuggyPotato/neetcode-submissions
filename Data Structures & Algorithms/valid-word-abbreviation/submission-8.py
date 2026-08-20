class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        def isDigit(digit):
            return digit <= '9' and digit >= '0'

        def readDigit(ptr2):
            start = ptr2
            while ptr2 < len(abbr) and isDigit(abbr[ptr2]):
                ptr2 += 1
            return abbr[start:ptr2]
        

        ptr1 = 0
        ptr2 = 0

        while ptr2 < len(abbr):
            if ptr1 >= len(word):
                return False

            if word[ptr1] == abbr[ptr2]:
                ptr1 += 1
                ptr2 += 1
                continue
            elif isDigit(abbr[ptr2]):
                if abbr[ptr2] != '0':
                    full_num = readDigit(ptr2)
                    ptr1 += int(full_num)
                    ptr2 += len(full_num)
                else:
                    return False
            else:
                return False

        return ptr1 == len(word)