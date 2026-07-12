class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            #left sorted?
            if nums[low]<=nums[mid]:
                #if yes
                #does it exist in left sorted part
                if nums[low] <= target < nums[mid]:
                    high=mid-1
                #if no
                else:
                    low=mid+1
            # Right half is sorted
            else:

            # Target lies in the right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1

            # Target lies in the left half
                else:
                    high = mid - 1
        return -1

