class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:

            # Opening bracket
            if ch in "({[":
                stack.append(ch)

            # Closing bracket
            else:
                if len(stack) == 0:
                    return False

                if stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
        
