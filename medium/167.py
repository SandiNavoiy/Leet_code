class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """"""
        start = 0
        finish = len(numbers) - 1
        while True:
            temp = numbers[start] + numbers[finish]
            if temp == target:
                return [start + 1, finish + 1]
            elif temp > target:
                finish = finish - 1
            elif temp < target:
                start = start + 1


numbers = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(numbers, target))
