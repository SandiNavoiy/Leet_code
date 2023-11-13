class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        """Сделайте два массива равными, поменяв местами подмассивы"""
        if len(target) != len(arr):
            return False
        target.sort()
        arr.sort()

        if target == arr:
            return True

        else:
            return False


target = [3, 7, 9]
arr = [3, 7, 11]
s = Solution()
print(s.canBeEqual(target, arr))
