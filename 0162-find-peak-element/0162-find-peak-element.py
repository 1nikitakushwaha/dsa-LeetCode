class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < nums[mid + 1]:
                # Increasing slope → peak is on the right
                low = mid + 1
            else:
                # Decreasing slope → peak is on the left (including mid)
                high = mid

        return low 