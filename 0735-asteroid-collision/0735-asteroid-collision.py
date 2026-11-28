class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for num in asteroids:
            if num > 0:
                stack.append(num)

            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(num):
                    stack.pop()

                if stack and stack[-1] == abs(num):
                    stack.pop()

                elif not stack or stack[-1] < 0:
                    stack.append(num)

        return stack
