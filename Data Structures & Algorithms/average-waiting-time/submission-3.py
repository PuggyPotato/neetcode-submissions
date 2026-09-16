class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current = 0
        waiting = 0

        for arrival, finished in customers:
            current = max(current, arrival) + finished

            waiting += current - arrival

        return waiting / len(customers)