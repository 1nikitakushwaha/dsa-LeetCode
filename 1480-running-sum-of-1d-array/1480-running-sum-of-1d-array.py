class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            ans.append(sum)
        return ans

