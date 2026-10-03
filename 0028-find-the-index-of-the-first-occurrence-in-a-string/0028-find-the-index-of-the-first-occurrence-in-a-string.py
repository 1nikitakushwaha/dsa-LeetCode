class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle not in haystack:
        #     return -1
        # for i in range(len(haystack)):
        #     for j in range(len(needle)):
        #         if haystack[i+j]==needle[j]
        
        for i in range(len(haystack) - len(needle) + 1):

            match = True

            for j in range(len(needle)):

                if haystack[i + j] != needle[j]:
                    match = False
                    break

            if match:
                return i

        return -1