class Solution:
    def myAtoi(self, s: str) -> int:
       
        i = 0
        n = len(s)
        sign = 1
        num = 0

        # 1. Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # 2. Check the sign
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        # 3. If no digit follows, return 0
        if i >= n or not s[i].isdigit():
            return 0

        # 4. Build the number
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1

        # 5. Apply the sign
        num = num * sign

        # 6. Handle 32-bit integer limits
        if num > 2147483647:
            return 2147483647
        if num < -2147483648:
            return -2147483648

        return num