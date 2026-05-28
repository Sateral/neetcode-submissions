class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        counterPart = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in counterPart:
                if stack and stack[-1] == counterPart[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        print(stack)

        return True if not stack else False