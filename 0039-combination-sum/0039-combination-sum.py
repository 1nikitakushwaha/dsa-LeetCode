class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        def backtracking(index,curr,sum):
            if sum==target:
                result.append(curr[:])
                return

            elif index==len(candidates) or sum>target:
                return
                
            curr.append(candidates[index])
            sum+=candidates[index]
            backtracking(index,curr,sum)

            curr.pop()
            sum-=candidates[index]
            backtracking(index+1,curr,sum)
        backtracking(0,[],0)  
        return result