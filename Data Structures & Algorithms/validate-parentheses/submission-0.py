class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        validParanthesis = {'{':'}', '[':']', '(':')'}
        openingBraces = []
        for i in s:
            if i in '({[':
                openingBraces.append(i)
            else:
                if openingBraces and i == validParanthesis.get(openingBraces[-1], False):
                    openingBraces.pop()
                else:
                    return False
        return len(openingBraces) == 0