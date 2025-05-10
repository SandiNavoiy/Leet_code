class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        '''Минимальное количество операций, чтобы сделать сумму массива делящейся на K'''
        n = 0
        s = sum(nums)
        while True:
            if s % k == 0:
                return n
            else:
                s -=1
                n = n + 1


s = Solution()
print(s.minOperations([3,9,7], 5))
