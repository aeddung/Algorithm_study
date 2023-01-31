class MyQueue:

    def __init__(self):
        self.inn = list()
        self.out = list()

    def push(self, x: int) -> None:
        self.inn.append(x)

    def pop(self) -> int:
        if len(self.out) == 0:
            while len(self.inn):
                self.out.append(self.inn.pop())
        return self.out.pop()

    def peek(self) -> int:
        if len(self.out) == 0:
            while len(self.inn):
                self.out.append(self.inn.pop())
        return self.out[len(self.out) - 1]

    def empty(self) -> bool:
        return len(self.inn) == 0 and len(self.out) == 0
