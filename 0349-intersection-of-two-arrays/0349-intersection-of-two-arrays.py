class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1=set(nums1)
        set2=set()

        for num in nums2:
            if num in set1:
                set2.add(num)
        return list(set2)
            