class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []

        for x in nums1:
            for i in range(len(nums2)):
                if nums2[i] == x:
                    for j in range(i+1, len(nums2)):
                        if nums2[j] > x:
                            result.append(nums2[j])
                            break
                    else:
                        result.append(-1)
                    break

        return result
