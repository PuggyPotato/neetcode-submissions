class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        string = ""

        for val in order:
            if val in counter:
                for i in range(counter[val]):
                    string += val
                del(counter[val])

        for val in counter:
            for i in range(counter[val]):
                string += val


        return string