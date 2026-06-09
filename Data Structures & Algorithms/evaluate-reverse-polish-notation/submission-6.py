import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op_map = {
            '+':lambda a,b: a+b,
            '-':lambda a,b: a-b,
            '*':lambda a,b: a*b,
            '/':lambda a,b: int(a/b), # 3/6 = 0.5 int will round them closest to the zero
        }

        for ele in tokens:
            if ele in op_map and len(stack)>1:
                num2 = stack.pop() 
                num1 = stack.pop()

                op = op_map[ele]
                stack.append(op(int(num1),int(num2)))
            else:
                stack.append(ele)



        if stack:
            print(stack)
            res = stack.pop()
            print(res)
            return int(res)