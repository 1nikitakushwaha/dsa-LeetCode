class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        curr = []

        def isPalindrome(word):
            return word == word[::-1]

        def backtrack(index):

            if index == len(s):
                result.append(curr[:])
                return

            for i in range(index, len(s)):

                substring = s[index:i+1]

                if isPalindrome(substring):
                    curr.append(substring)

                    backtrack(i + 1)

                    curr.pop()

        backtrack(0)
        return result