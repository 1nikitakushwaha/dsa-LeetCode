class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping={}
        mapping2 = {} 

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            chr_s=s[i]
            chr_t=t[i]
            if chr_s in mapping:
                if mapping[chr_s]!=chr_t:
                    return False
            else:
                mapping[chr_s]=chr_t
            # Check mapping in both directions to ensure a one-to-one relationship
            #s = "ab"
            #t = "cc"
            if chr_t in mapping2:
                if mapping2[chr_t] != chr_s:
                    return False
            else:
                mapping2[chr_t] = chr_s
        return True

