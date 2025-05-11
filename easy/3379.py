class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        """Преобразованный массив"""
        l = len(nums)
        rez = [0] * l
        for i in range(l):
            if nums[i] > 0:
                temp = (i + nums[i]) % l
                if temp > l - 1:
                    rez[i] = nums[temp - l]
                else:
                    rez[i] = nums[temp]

            elif nums[i] < 0:
                temp = (i + nums[i]) % l
                rez[i] = nums[temp]
            else:
                rez[i] = nums[i]
            print(rez)
        return rez


s = Solution()
print(s.constructTransformedArray(nums=[-10]))
