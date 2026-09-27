class Solution:
    def tribonacci(self, n: int) -> int:
        x,y,z = 0,1,1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        for _ in range(2,n):
            x,y,z = y, z, x + y + z

        return z