class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashmap = {}

        for val in nums:
            hashmap[val] = hashmap.get(val, 0) + 1

        result = []
        for key, val in hashmap.items():
            if val == 1:
                result.append(key)
        return result