class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        """Перестановка массива путем удаления неуникальных значений."""
        ans = []

        while nums:
            temp = []
            nums1 = []
            for i in nums:
                if i not in temp:
                    temp.append(i)
                else:
                    nums1.append(i)

            nums = nums1
            ans.extend(sorted(temp))

        return  ans



s = Solution()
print(s.rearrangeArray([3,1,3,2,1,3]))
