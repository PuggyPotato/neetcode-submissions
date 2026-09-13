class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:    

        ptr = 0
        time = 0

        while tickets[k] > 0:

            if tickets[ptr] > 0:
                tickets[ptr] -= 1
                time += 1
                
            ptr += 1

            if ptr >= len(tickets):
                ptr = 0

        return time

