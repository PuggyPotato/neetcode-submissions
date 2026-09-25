class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2147483647

        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            if result > max_int // 10 or (result == max_int // 10 and digit > 7):
                return 0
            
            result = result * 10 + digit

        return sign * result
