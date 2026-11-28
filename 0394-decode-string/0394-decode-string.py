class Solution:
    def decodeString(self, s: str) -> str:
        no = []
        string = []
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                no.append(num)
                num = 0
                string.append(ch)

            elif ch != "]":
                string.append(ch)

            if ch == "]" and len(string) != 0:
                curr = ""
                while string and string[-1] != "[":
                    curr = string[-1] + curr
                    string.pop()

                string.pop()

                n = no.pop()
                curr = curr * n
                string.append(curr)

        return "".join(string)