class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #brute force
        if len(s)!=len(goal):
            return False
        curr_s=s
        for i in range(len(s)):
            if curr_s==goal:
                return True
            else:
                curr_s=curr_s[-1]+curr_s[:-1]
        return False



        # if len(s)!=len(goal):
        #     return False
        # new=s+s #O(N)
        # if goal in new:  #O(N)
        #     return True
        # return False

        # #TC=O(2N)
        # #SC=O(2N)