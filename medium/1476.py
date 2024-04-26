class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
        self.rectangles =rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1,row2+1):
            for j in range(col1, col2+1):
                self.rectangles[i][j] = newValue
        print(self.rectangles)

    def getValue(self, row: int, col: int) -> int:
        return self.rectangles[row][col]




rectangle = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]]
# Your SubrectangleQueries object will be instantiated and called as such:
obj = SubrectangleQueries(rectangle)
row1,col1,row2,col2,newValue = (0, 0, 3, 2, 5)

obj.updateSubrectangle(row1,col1,row2,col2,newValue)

row = 0
col = 2
param_2 = obj.getValue(row,col)
print(param_2)