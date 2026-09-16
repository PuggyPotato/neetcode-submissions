class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_elapsed = customers[0][0] + customers[0][1]
        waiting = customers[0][1]

        for i in range(1, len(customers)):
            if total_elapsed > customers[i][0]:
                waiting += total_elapsed - customers[i][0] + customers[i][1]
            else:
                waiting += customers[i][1]

            if total_elapsed < customers[i][0]:
                total_elapsed += (customers[i][0] - total_elapsed)

            total_elapsed += customers[i][1]
            
        return waiting / len(customers)