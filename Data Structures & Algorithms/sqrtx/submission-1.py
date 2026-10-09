class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x

        while l <= r:
            mid = (l + r) // 2

            val = mid * mid
            if val <= x and ((mid + 1) * (mid + 1) > x) and ((mid - 1) * (mid - 1) < x):
                return mid
            elif val > x:
                r = mid - 1
            else:
                l = mid + 1

        return 0
