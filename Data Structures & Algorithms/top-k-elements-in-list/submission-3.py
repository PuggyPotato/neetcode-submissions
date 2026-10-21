class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array = [0] * 2001
        result = []

        for val in nums:
            array[val + 1000] += 1

        index = 0
        for i in range(k):
            max_val = 0

            for j, val in enumerate(array):
                if val > max_val:
                    max_val = max(max_val, val)
                    index = j

            result.append(index - 1000)
            array[index] = 0

        return result

                

            
