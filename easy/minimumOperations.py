class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        """Сделать массив нулевым, вычитая равные суммы"""
        wer = []
        for i in nums:
            if i != 0:
                wer.append(i)
        iter = len(set(wer))
        return iter


nums = [1, 5, 0, 3, 5]
s = Solution()
print(s.minimumOperations(nums))
