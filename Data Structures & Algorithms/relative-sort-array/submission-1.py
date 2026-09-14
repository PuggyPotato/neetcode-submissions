class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []

        counter = Counter(arr1)

        for val in arr2:
            result.extend([val] * counter[val])

            del counter[val]

        
        for key, val in sorted(counter.items(), key = lambda item: item[0]):
            result.extend([key] * val)

        return result  
