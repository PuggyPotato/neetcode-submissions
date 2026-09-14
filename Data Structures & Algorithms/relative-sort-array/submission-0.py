class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []

        counter = Counter(arr1)

        for val in arr2:
            for i in range(counter[val]):
                result.append(val)

            del counter[val]

        
        for key, val in sorted(counter.items(), key = lambda item: item[0]):
            for i in range(val):
                result.append(key)

        return result  
