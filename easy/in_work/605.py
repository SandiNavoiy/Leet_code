class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        ''''''

        if len(flowerbed) == 0:
            return False
        elif len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        elif len(flowerbed) == 1 and flowerbed[0] == 1 and n == 0:
            return True
        x = 0
        i = 1
        end = len(flowerbed)
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            i = 2
            x = x + 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            end = end -1
            x = x + 1

        while i <= end-1:
            if flowerbed[i] == 0 and flowerbed[max(i-1, 0)] == 0 and flowerbed[min(i+1,  end)] == 0:
                x = x + 1
                i = i + 2
            else:
                i = i + 1
        print(x)

        return x >= n
flowerbed = [0]
n = 1
s = Solution()
print(s.canPlaceFlowers(flowerbed, n))