class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def backtracking(index, curr, total):

            if total == target:
                result.append(curr[:])
                return

            if index == len(candidates) or total > target:
                return

            # PICK
            curr.append(candidates[index])
            backtracking(index + 1, curr, total + candidates[index])

            # UNDO
            curr.pop()

            # SKIP duplicates
            next_index = index + 1

            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1

            # SKIP
            backtracking(next_index, curr, total)

        backtracking(0, [], 0)
        return result
        # candidates.sort()
        # result = set()

        # def backtracking(index, curr, total):

        #     if total == target:
        #         result.add(tuple(curr))
        #         return

        #     if index == len(candidates) or total > target:
        #         return

        #     # PICK
        #     curr.append(candidates[index])
        #     backtracking(index + 1, curr, total + candidates[index])

        #     # UNDO
        #     curr.pop()

        #     # SKIP
        #     backtracking(index + 1, curr, total)

        # backtracking(0, [], 0)

        # return [list(x) for x in result]

        # result=[]
        # def backtracking(index,curr,sum):
        #     if sum==target:
        #         result.append(curr[:])
        #         return

        #     elif index==len(candidates) or sum>target: #CANT DO THIS WE WANT TO MAKE IT  FROM   STARTING NOT AFTER CREATING THE RESULT
        #         return
                
        #     curr.append(candidates[index])
        #     sum+=candidates[index]
        #     backtracking(index+1,curr,sum)

        #     curr.pop()
        #     sum-=candidates[index]
        #     backtracking(index+1,curr,sum)
        # backtracking(0,[],0)  

        # unique = set()

        # for sub in result:
        #     unique.add(tuple(sorted(sub)))

        # ans = [list(x) for x in unique]
        # return ans
        