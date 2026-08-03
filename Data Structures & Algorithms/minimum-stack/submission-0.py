class MinStack:

    def __init__(self):
        #stack to store the actual elements
        self.stack = []
        #keep track of minimum elements
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or self.minstack[-1] >= val:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.minstack[-1]:
                self.minstack.pop()
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        
