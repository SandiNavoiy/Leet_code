class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        s = 0
        c = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        for i in boxTypes:
            if c >= truckSize:
                break
            num_boxes = min(i[0], truckSize - c)
            s += num_boxes * i[1]
            c += num_boxes
        return s


boxTypes = [[1, 3], [2, 2], [3, 1]]
TruckSize = 4
s = Solution()
print(s.maximumUnits(boxTypes, TruckSize))
