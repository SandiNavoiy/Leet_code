class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        """"""
        chet = []
        nechet = []
        new = []
        for i in range(len(nums)):
            if i % 2 == 0:
                chet.append(nums[i])
            else:
                nechet.append(nums[i])
        nechet.sort(reverse=True)
        chet.sort()
        print(chet)
        print(nechet)

        y = 0
        z = 0
        for i in range(len(nums)):

            if i % 2 == 0:
                new.append(chet[y])
                y += 1

            else:
                new.append(nechet[z])
                z += 1

        return new


nums = [36, 45, 32, 31, 15, 41, 9, 46, 36, 6, 15, 16, 33, 26, 27, 31, 44, 34]
s = Solution()
print(s.sortEvenOdd(nums))
