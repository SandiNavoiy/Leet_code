class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        '''Общая волнистость чисел в диапазоне I'''
        n = 0

        for num in range(num1, num2 + 1):
            if num < 100:

                continue
            num = str(num)
            for j in range(1, len(str(num))-1):
                if num[j-1] < num[j] > num[j+1]:
                    n = n + 1

                if num[j - 1] > num[j] < num[j + 1]:
                    n = n + 1

        return n




s = Solution()
print(s.totalWaviness(num1=9895, num2=9950))
