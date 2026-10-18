class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_ship_in_time(capacity):
            days_needed = 1
            current_weight = 0

            for w in weights:

                if current_weight + w > capacity:
                    days_needed += 1
                    current_weight = w
                else:
                    current_weight += w

            return days_needed <= days

        left,right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2

            if can_ship_in_time(mid):
                right = mid
            else:
                left = mid + 1

        return left
            

            