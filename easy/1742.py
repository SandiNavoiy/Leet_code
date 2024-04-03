import collections


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ballBox = collections.defaultdict(int)

        for i in range(lowLimit, highLimit + 1):
            ballSum = sum([int(i) for i in str(i)])
            ballBox[ballSum] += 1

        return max(ballBox.values())


lowLimit = 1
highLimit = 10
s = Solution()
print(s.countBalls(lowLimit, highLimit))
