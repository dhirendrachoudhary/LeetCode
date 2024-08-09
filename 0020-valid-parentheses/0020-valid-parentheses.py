class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = False
        for bra in s:
            if len(stack) == 0:
                stack.append(bra)
            else:
                if stack[-1] == '(' and bra == ')':
                    stack.pop()
                elif stack[-1] == '[' and bra == ']':
                    stack.pop()
                elif stack[-1] == '{' and bra == '}':
                    stack.pop()
                else:
                    stack.append(bra)
        return True if len(stack) == 0 else False