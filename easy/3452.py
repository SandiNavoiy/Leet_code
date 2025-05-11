class Solution:
    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        """Сумма хороших чисел"""

        rez = []
        l = len(nums)
        for i in range(l):
            left = i - k
            right = i + k
            if left >= 0 and right < l:
                if nums[i] > nums[left] and nums[i] > nums[right]:
                    rez.append(nums[i])
            elif left < 0 and right < l:
                if nums[i] > nums[right]:
                    rez.append(nums[i])
            elif left >= 0 and right >= l:
                if nums[i] > nums[left]:
                    rez.append(nums[i])

        return sum(rez)


s = Solution()
print(s.sumOfGoodNumbers(nums=[1, 3, 2, 1, 5, 4], k=2))
