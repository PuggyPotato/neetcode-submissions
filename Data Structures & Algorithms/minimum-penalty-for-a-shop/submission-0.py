class Solution:
    def bestClosingTime(self, customers: str) -> int:
        total = customers.count("Y")
        minimum = total
        min_hour = 0

        for i, val in enumerate(customers):
            if val == "Y":
                total -= 1
            elif val == "N":
                total += 1
            
            if total < minimum:
                minimum = total
                min_hour = i + 1

        return min_hour