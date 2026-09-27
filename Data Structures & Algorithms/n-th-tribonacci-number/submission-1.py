class Solution:
    def tribonacci(self, n: int) -> int:
        x,y,z = 0,1,1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        for i in range(2,n):
            x = x + y + z
            x,z = z,x
            x,y = y,x

        return z


        #0 1 1
        #0 1 1 2
        #0 1 1 2 4
        #0 1 1 2 4 7
        #0 1 1 2 4 7 13

        #0 1 1
        #1 1 2
        #1 2 4
        #2 4 7
        #4 7 13