class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = []
        for key, value in sorted(counter.items(), key=lambda item:(item[1], -item[0])):
            for i in range(value):
                result.append(key)

        return result