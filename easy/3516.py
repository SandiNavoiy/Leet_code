class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        """Найти ближайшего человека"""

        if abs(z - x) < abs(z - y):
            return 1
        elif abs(z - x) > abs(z - y):
            return 2
        else:
            return 0


s = Solution()
print(s.findClosest(x=2, y=7, z=4))
