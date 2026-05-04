class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c not in mapping:
                stack.append(c)
            elif stack and mapping[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return True if len(stack) == 0 else False
