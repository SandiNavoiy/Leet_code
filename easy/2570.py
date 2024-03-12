class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        ''''''
        x = {}
        rez = []
        for i in nums1 + nums2:
            if i[0] not in x:
                x[i[0]] = 0
            x[i[0]] = x[i[0]] + i[1]
        for a,b in x.items():
           rez.append([a,b])
        rez.sort()
        return rez

nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
s = Solution()
print(s.mergeArrays(nums1, nums2))