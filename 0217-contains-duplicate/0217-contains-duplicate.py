class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dic={}
        # for num in nums:
        #     if num in dic:
        #         dic[num]+=1
        #     else:
        #         dic[num]=1
        # for num,count in dic.items():
        #     if count>1:
        #       return True
        # return False

        seen=set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
            
        
        