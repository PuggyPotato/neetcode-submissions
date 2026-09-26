class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        x = 1
        y = 2

        for i in range(2, n):
            x = x + y
            x,y = y,x

        return y


# 1 = 1
# 2 = 1 + 1, 2
# 3 = 1+1+1, 1+2, 2+1
# 4 = 2 + 2, 1+1+1+1, 2+1+1, 1+2+1, 1+1+2