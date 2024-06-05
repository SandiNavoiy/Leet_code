class BrowserHistory:

    def __init__(self, homepage: str):
        self.links = [homepage]
        self.ind = 0
        self.size = 1

    def visit(self, url: str) -> None:
        if self.ind + 1  >=  len(self.links):
            self.links.append(url)
        else:
            self.links[self.ind + 1] = url


        self.ind += 1
        self.size = self.ind + 1

    def back(self, steps: int) -> str:
        self.ind = max(0, self.ind - steps)
        return self.links[self.ind]

    def forward(self, steps: int) -> str:
        self.ind = min(self.size - 1, self.ind + steps)
        return self.links[self.ind]

# Your BrowserHistory object will be instantiated and called as such:
homepage = "1"
obj = BrowserHistory(homepage)
url = "2"
obj.visit(url)
url = "3"
obj.visit(url)
url = "4"
obj.visit(url)
url = "5"
obj.visit(url)
print(obj.links)
steps = 2
param_2 = obj.back(steps)
print(param_2)
steps = 1
param_3 = obj.forward(steps)
print(param_3)