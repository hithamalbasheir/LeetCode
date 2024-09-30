class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = deque([])
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) >= self.size:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if not self.stack: return
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)