class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for i, interval in enumerate(self.events):
            s, e = interval
            if not (e <= start or end <= s):
                for s_s, s_e in self.events[i+1:]:
                    if not (s_e <= start or end <= s_s) and not (s_e <= s or e <= s_s):
                        return False
        self.events.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)