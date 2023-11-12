class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        """Самоделящиеся числа"""
        new = []
        for i in range(left, right + 1):
            print(i)
            for j in str(i):
                if int(j) != 0:
                    if i % int(j) == 0:
                        new.append(i)



        return list(set(new))

left = 47
right = 85
s = Solution()
print(s.selfDividingNumbers(left, right))
#[48,55,66,77]