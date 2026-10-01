class Solution:
    def longestConsecutive(self, nums: List[int]):

        # #brute force Brute Force — O(n²)

        # s = set(nums)

        # longest = 0

        # for num in s:

        #     if num - 1 not in s:

        #         current = num
        #         length = 1

        #         while current + 1 in s:
        #             current += 1
        #             length += 1

        #         longest = max(longest, length)

        # return longest
    #Sorting — O(n log n)
            nums.sort()
            largest=0
            count=0
            last_smaller=float('-inf')
            for i in range(len(nums)):
                num=nums[i]
                if num-1==last_smaller:
                    count+=1
                    last_smaller=num
                elif num!=last_smaller:
                    count=1
                    last_smaller=num
                largest=max(largest,count)
            return largest
