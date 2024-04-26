class RecentCounter:
    def __init__(self):
        self.data = []

    def ping(self, t: int) -> int:
        self.data.append(t)
        if t - 3000 < 0:
            return len(self.data)

        else:
            temp = []
            for i in self.data:
                if i >= t - 3000:
                    temp.append(i)
            return len(temp)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
