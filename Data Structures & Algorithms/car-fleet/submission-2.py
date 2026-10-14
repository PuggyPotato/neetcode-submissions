class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        diff = 0
        largest = -1  

        for pos, spd in sorted(zip(position, speed), reverse=True):
            count = (target - pos) / spd
            if count > largest:
                diff += 1
                largest = count  

        return diff