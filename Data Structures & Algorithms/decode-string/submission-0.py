class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)

            else:
                substring = ""

                while stack[-1] != "[":
                    substring = stack.pop() + substring

                stack.pop()

                number = ""

                while stack and stack[-1].isdigit():
                    number = stack.pop() + number

                stack.append(substring * int(number))

        return "".join(stack)