class Solution:
    def intToRoman(self, num: int) -> str:

        four = ""
        three = ""
        two = ""
        one = ""

        if num >= 1:
            last = num % 10
            while last > 0:
                if last - 9 >= 0:
                    four += "IX"
                    last -= 9
                elif last - 5 >= 0:
                    four += "V"
                    last -= 5
                elif last - 4 >= 0:
                    four += "IV"
                    last -= 4
                else:
                    four += "I"
                    last -= 1
        
        if num >= 10:
            last = (num // 10) % 10
            while last > 0:
                if last - 9 >= 0:
                    three += "XC"
                    last -= 9
                elif last - 5 >= 0:
                    three += "L"
                    last -= 5
                elif last - 4 >= 0:
                    three += "XL"
                    last -= 4
                else:
                    three += "X"
                    last -= 1

        if num >= 100:
            last = (num // 100) % 10
            while last > 0:
                if last - 9 >= 0:
                    two += "CM"
                    last -= 9
                elif last - 5 >= 0:
                    two += "D"
                    last -= 5
                elif last - 4 >= 0:
                    two += "CD"
                    last -= 4
                else:
                    two += "C"
                    last -= 1

        if num >= 1000:
            last = (num // 1000) % 10
            while last > 0:
                one += "M"
                last -= 1

        return one + two + three + four

