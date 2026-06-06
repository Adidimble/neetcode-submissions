class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        #maintain the mini at each level of the stack 
        
        if self.mini:
            if self.mini[-1] > val:
                self.mini.append(val)
            else:
                self.mini.append(self.mini[-1])

        else:
            self.mini.append(val)


            
        

    def pop(self) -> None:
        if self.stack:
            element = self.stack.pop(-1)
            self.mini.pop(-1)
            return element
        else:
            return None

        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self) -> int:
        if self.mini:
            return self.mini[-1]

        
