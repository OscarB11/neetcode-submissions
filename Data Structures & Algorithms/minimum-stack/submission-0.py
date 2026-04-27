class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:

        self.stack.append(val)
        if self.minstack:
            mi = min(val,self.minstack[-1])
        else:
            mi = val
        self.minstack.append(mi)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
