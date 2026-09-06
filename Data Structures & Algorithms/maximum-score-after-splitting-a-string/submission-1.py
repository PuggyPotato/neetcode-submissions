class Solution:
    def maxScore(self, s: str) -> int:
        count_a = []
        count_b = []

        count = 0
        for i in range(len(s) -1):
            if s[i] == "0":
                count += 1

            count_a.append(count)
            
        count = 0

        for i in range(len(s) - 1, 0, -1):
            if s[i] == "1":
                count += 1

            count_b.append(count)

        maximum = 0
        print(count_a, count_b)

        for i in range(len(count_a)):
            maximum = max(maximum, (count_a[0-i] + count_b[i]))
            


        return maximum
                 