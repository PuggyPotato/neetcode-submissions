import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        for i in range(k):
            index = gifts.index(max(gifts))
            gifts[index] = math.floor(math.sqrt(gifts[index]))

        return sum(gifts)