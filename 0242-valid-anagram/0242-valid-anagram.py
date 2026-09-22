class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dic_s={}
        # dic_t={}
        # for ch in s:
        #     if ch in dic_s:
        #         dic_s[ch]+=1
        #     else:
        #         dic_s[ch]=1
        # for ch in t:
        #     if ch in dic_t:
        #         dic_t[ch]+=1
        #     else:
        #         dic_t[ch]=1 
        # if dic_s==dic_t:
        #     return True
        # else:
        #     return False

        #using optimal solution o(1)=sc tc=o(n)
        
        if len(s)!=len(t):
            return False
        freq=[0]*26
        for ch in s:
            freq[ord(ch)-ord("a")]+=1
        for ch in t:
            freq[ord(ch)-ord("a")]-=1
        for count in freq:
            if count!=0:
                return False
            
        return True
        