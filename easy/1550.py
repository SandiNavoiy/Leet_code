class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        ''''''
        x = 0
        for i in arr:
            if i % 2 != 0:
                x += 1

                if x == 3:
                    return True
            else:
                x = 0
        return False

arr = [1,2,34,3,4,5,7,23,12]
s = Solution()
print(s.threeConsecutiveOdds(arr))