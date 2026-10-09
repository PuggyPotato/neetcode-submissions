class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x

        while l <= r:
            mid = (l + r) // 2

            square = mid * mid
            if square <= x < (mid + 1) * (mid + 1):
                return mid
            elif square > x:
                r = mid - 1
            else:
                l = mid + 1

        return 0
