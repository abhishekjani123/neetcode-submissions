class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        l = {')': '(', ']' : '[', '}':'{'}

        for c in s:
            if c in l:
                if stack and stack[-1] == l[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0