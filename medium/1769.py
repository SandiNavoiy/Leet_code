class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        rez = []

        for i in range(len(boxes)):
            temp = 0
            for j in range(i, len(boxes)):
                if boxes[j] == '1':
                    temp += j - i
            for j in range(0, i):
                if boxes[j] == '1':
                    temp += abs(j - i)
            rez.append(temp)




        return rez



boxes = "110"
s = Solution()
print(s.minOperations(boxes))