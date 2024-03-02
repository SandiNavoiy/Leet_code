class Solution:
    def findLucky(self, arr: list[int]) -> int:
        ''''''
        x = 0
        char = 0
        for i in arr:
            if arr.count(i) > x and arr.count(i) == i:
                x = arr.count(i)
                char = i
        if char == 0:
            return -1
        return char


arr = [2,2,3,4]
s = Solution()
print(s.findLucky(arr))