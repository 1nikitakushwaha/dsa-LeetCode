class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result=[[]]
        for num in nums:
            for i in range(len(result)):
                result.append(result[i]+[num])
        return result 

        # Initially:
# result = [[]]

# num = 1
# i = 0 -> result[0] = []
# [] + [1] = [1]
# result = [[], [1]]

# num = 2
# len(result) = 2, so i = 0, 1
# i = 0 -> [] + [2] = [2]
# result = [[], [1], [2]]
# i = 1 -> [1] + [2] = [1, 2]
# result = [[], [1], [2], [1, 2]]

# num = 3
# len(result) = 4, so i = 0, 1, 2, 3
# i = 0 -> [] + [3] = [3]
# i = 1 -> [1] + [3] = [1, 3]
# i = 2 -> [2] + [3] = [2, 3]
# i = 3 -> [1, 2] + [3] = [1, 2, 3]

# Final result:
# [[], [1], [2], [1, 2], [3],
#  [1, 3], [2, 3], [1, 2, 3]]