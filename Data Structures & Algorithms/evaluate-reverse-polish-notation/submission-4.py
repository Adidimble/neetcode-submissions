import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op_map = {
            '+':lambda a,b: a+b,
            '-':lambda a,b: a-b,
            '*':lambda a,b: a*b,
            '/':lambda a,b: a/b,
        }

        for ele in tokens:
            if ele in op_map and len(stack)>1:
                num2 = stack.pop() 
                num1 = stack.pop()

                result = eval(f"{num1} {ele} {num2}")
                if isinstance(result,float):
                    result = math.floor(result) if result >=0 else math.ceil(result) 

                stack.append(result)
                print(result)
            else:
                stack.append(ele)



        if stack:
            print(stack)
            res = stack.pop()
            print(res)
            return int(res)