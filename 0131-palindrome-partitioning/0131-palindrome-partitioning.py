class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        curr = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(index):
            if index == len(s):          # whole string used
                res.append(curr[:])      # save a copy
                return

            for i in range(index, len(s)):
                if isPalindrome(index, i):
                    curr.append(s[index:i+1])   # choose
                    backtrack(i + 1)            # explore
                    curr.pop()                  # un-choose

        backtrack(0)
        return res