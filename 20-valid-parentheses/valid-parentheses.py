class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        obj = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in obj:
                stack.append(bracket)
            else:
                if len(stack) > 0:
                    temp = stack.pop()
                    if obj[temp] != bracket:
                            return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False