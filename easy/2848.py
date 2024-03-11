class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        ''''''
        x = set()
        for a,b  in nums:
            for j in range(a, b + 1):
                x.add(j)

        return len(x)



nums = [[3,6],[1,5],[4,7]]
s = Solution()
print(s.numberOfPoints(nums))