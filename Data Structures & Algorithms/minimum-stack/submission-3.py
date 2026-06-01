class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []
        self.current_min = float('inf')

    def push(self, val: int) -> None:
        self.st.append(val)
        self.current_min = min(self.current_min, val)
        self.min_st.append(self.current_min)

    def pop(self) -> None:
        self.st.pop()
        self.min_st.pop()
        if len(self.min_st) > 0:
            self.current_min = self.getMin()
        else:
            self.current_min = float('inf')

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
