class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = [0] * 101
        count = 0
        for val in heights:
            arr[val] += 1

        height_count = 0
        for val in heights:
            while arr[height_count] == 0:
                height_count +=1
            
            if val != height_count:
                count += 1

            arr[height_count] -= 1

        return count 