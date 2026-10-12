class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)

        count = 0
        for val in counter.values():

            while val > 0:

                if val == 1:
                    return -1

                if val % 3 == 0:
                    count += val // 3
                    break

                elif val % 3 == 1:
                    count += 1
                    val -= 2
                
                elif val % 3 == 2:
                    count += val // 3
                    count += 1
                    break
            
            

        return count
                