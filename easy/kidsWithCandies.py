class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans = []

        for i in candies:
            if (i + extraCandies) >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans

candies = [4,2,1,1,2]
extraCandies = 1
s = Solution()
print(s.kidsWithCandies(candies, extraCandies))
#[true,true,true,false,true]
