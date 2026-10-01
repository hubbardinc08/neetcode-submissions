class MinStack:

    def __init__(self):
        self.min = []
        self.currIndex = 0
        self.nums = []

    def push(self, val: int) -> None:
        if (self.currIndex >= len(self.nums)):
            self.nums.append(val)
            self.currIndex += 1
        else:
            self.nums[self.currIndex] = val
            self.currIndex += 1
        
        if (len(self.min) == 0):
            self.min.append(val)
            return

        if (val < self.min[-1]):
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        self.min.pop()
        self.currIndex -= 1

    def top(self) -> int:
        return self.nums[self.currIndex - 1]

    def getMin(self) -> int:
        elem = self.min[-1]
        return elem 
        
