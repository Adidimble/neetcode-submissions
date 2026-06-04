class Solution:

    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(','}':'{',']':'['}
        stack = []


        for c in s:
            #check agar element closed bracket hai
            if c in closeToOpen:
                #check stack is not empty and stack ka top is equal to opening of that closing jo milega closetoopen[')'] = (
                #stack ka top = '(' if both same then pop
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                #opening bracket hai add karo
                stack.append(c)
        
        return True if not stack else False
