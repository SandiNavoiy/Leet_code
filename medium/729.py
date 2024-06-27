class MyCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for i in self.calendar:
            if i[0] <= start < i[1] or i[0] < end <= i[1]:
                return False
            if i[0] > start and i[1] < end:
                return False
        self.calendar.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()

start = 10
end = 20
param_1 = obj.book(start, end)
print(param_1)
