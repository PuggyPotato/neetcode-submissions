class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            last = n & 1
            result = result | last << (31 -i)
            n = n >> 1

        return result