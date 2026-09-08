class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = [0] * (len(nums) + 1)
        result = [0] * 2

        for num in nums:
            freq[num] += 1

        for i in range(len(freq)):
            if freq[i] == 2:
                result[0] = i

            if freq[i] == 0:
                result[1] = i

        return result


