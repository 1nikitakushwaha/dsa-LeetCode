class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = high

        while low <= high:

            mid = (low + high) // 2

            required_days = 1
            current_weight = 0

            for weight in weights:

                if current_weight + weight <= mid:
                    current_weight += weight
                else:
                    required_days += 1
                    current_weight = weight

            if required_days <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans