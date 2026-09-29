class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0
        count20 = 0

        for val in bills:
            if val == 5:
                count5 += 1
            elif val == 10:
                count10 += 1
                count5 -= 1
            elif val == 20:
                if count10 > 0:
                    count10 -= 1
                    count5 -= 1
                else:
                    count5 -= 3
            if count5 < 0 or count10 < 0:
                return False

        return True