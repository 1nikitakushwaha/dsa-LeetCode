class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #using recursion
        def bs(low, high):
            if low > high:
                return -1

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                return bs(mid + 1, high)
            else:
                return bs(low, mid - 1)

        return bs(0, len(nums) - 1)
            

            
        
        