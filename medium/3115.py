class Solution:
    def maximumPrimeDifference(self, nums: list[int]) -> int:
        ''''''

        def is_prime(a):
            if a > 1:
                k = 0
                for i in range(2, a // 2 + 1):
                    if (a % i == 0):
                        k = k + 1
                if (k <= 0):
                    return a


        new = []
        for i in range(len(nums)):
            x  =is_prime(nums[i])
            if x:
                new.append(i)

        print( new)
        return new[-1] - new[0]

nums = [1,7]
s = Solution()
print(s.maximumPrimeDifference(nums))