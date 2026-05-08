class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for char in s:
            if char == '[' or char == '(' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                if char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False