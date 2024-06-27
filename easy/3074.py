class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        ''''''
        capacity.sort(reverse=True)
        summ = sum(apple)
        print(summ)
        print(capacity)
        for i, val in enumerate(capacity):
            summ = summ - val
            if summ <= 0:
                return i+1



apple = [1,3,2]
capacity = [4,3,1,5,2]
s = Solution()
print(s.minimumBoxes(apple, capacity))