# 시간 600ms 소요
class MinStack:
    def __init__(self):
        self.__stack = []

    def push(self, val: int) -> None:
        self.__stack.append(val)

    def pop(self) -> None:
        self.__stack.pop()

    def top(self) -> int:
        if self.__stack:
            return self.__stack[-1]

    def getMin(self) -> int:
        return min(self.__stack)
      
# 시간 52ms 소요
class MinStack:
    def __init__(self):
        self.A = []
        self.M = []
        
    def push(self, x):
        self.A.append(x)
        M = self.M
        if not M:
            M.append(x)
        else:
            M.append(min(x, M[-1]))
        
    def pop(self):
        self.A.pop()
        self.M.pop()
        
    def top(self):
        return self.A[-1]
    
    def getMin(self):
        return self.M[-1]
