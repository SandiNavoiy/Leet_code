class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        """Найдите самую большую высоту"""
        new_gain = [0]
        sunn = 0
        for i in gain:
            sunn = i + sunn
            new_gain.append(sunn)
        return max(new_gain)


gain = [-5, 1, 5, 0, -7]
# [0,-5,-4,1,1,-6]
s = Solution()
print(s.largestAltitude(gain))
