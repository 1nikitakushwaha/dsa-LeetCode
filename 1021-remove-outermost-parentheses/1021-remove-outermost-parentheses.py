class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        count=0
        for chr in s:
            if chr=="(":
                count+=1
                if count>1:
                    ans+=chr

            if chr==")":
                if count>1:
                    ans+=chr
                count-=1
        return ans
            
            
            