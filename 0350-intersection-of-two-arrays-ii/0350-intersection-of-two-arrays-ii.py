class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[]
        for num in nums2:
          if num in nums1:
            ans.append(num)
            nums1.remove(num)
        return ans
        
            