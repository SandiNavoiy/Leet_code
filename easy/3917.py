class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        '''Count Indices With Opposite Parity'''
        rez = [0] * len(nums)
        col_nechet = 0
        col_chet = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] % 2 == 0:
                col_chet = col_chet + 1
                rez[i] =  col_nechet
            else:
                col_nechet = col_nechet + 1
                rez[i] = col_chet




        return rez

s = Solution()
print(s.countOppositeParity([1,2,3,4]))
