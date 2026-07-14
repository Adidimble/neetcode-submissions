class Solution:
    def isValid(self, s: str) -> bool:
        valid_bracket = {')':'(','}':'{',']':'['}
        stack = []
        for bracket in s:
            if bracket not in valid_bracket:
                stack.append(bracket)
            elif len(stack)>0 and stack[-1] ==  valid_bracket[bracket]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False
        