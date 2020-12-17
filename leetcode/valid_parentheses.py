class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i not in table:
                stack.append(i)
            elif stack and table[i] == stack.pop():
                continue
            else:
                return False

        if not stack:
            return True
        else:
            return False