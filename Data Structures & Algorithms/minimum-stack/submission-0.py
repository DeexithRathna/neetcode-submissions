class MinStack:

    def __init__(self):
        self.arr = []
        self.minvals = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.minvals:
            self.minvals.append(min(self.minvals[-1], val))
        else:
            self.minvals = [val]
        

    def pop(self) -> None:
        self.arr.pop()
        self.minvals.pop()
        


    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minvals[-1]
        
