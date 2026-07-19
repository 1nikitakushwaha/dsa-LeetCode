class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        while low <= high:

            mid = (low + high) // 2

            hours = 0

            for pile in piles:
                # Ceiling division
                hours += (pile + mid - 1) // mid

            if hours <= h:
                ans = mid          # Possible answer
                high = mid - 1     # Try smaller speed
            else:
                low = mid + 1      # Need higher speed

        return ans