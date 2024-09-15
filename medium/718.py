class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        ''''''
        dp = [[0]* (len(nums2)+1) for i in range(len(nums1) + 1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1


        return max(map(max, dp))
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
s = Solution()
print(s.findLength(nums1, nums2))