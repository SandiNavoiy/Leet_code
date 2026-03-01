from functools import reduce


class Solution:
    def evenNumberBitwiseORs(self, nums) -> int:
        """ПО БИТОВОЕ или"""


        chet = [i for i in nums if i%2==0]
        if len(chet)==0:
            return 0

        s = reduce(lambda x, y: x | y, chet)
        return s




s = Solution()
print(s.evenNumberBitwiseORs([7,9,11]))