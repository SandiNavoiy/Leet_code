class Solution:
    """Вычтите произведение и сумму цифр целого числа"""
    def subtractProductAndSum(self, n: int) -> int:
        new_str = str(n)
        multiplication  = 1
        sum = 0
        for i in new_str:
            multiplication  = multiplication * int(i)
            sum = sum + int(i)


        return multiplication - sum

n = 234
s = Solution()
print(s.subtractProductAndSum(n))
