class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        """Может сделать арифметическую прогрессию из последовательности"""
        arr.sort()
        list_chek = []
        for i in range(0, len(arr) - 2):
            if arr[i] - arr[i + 1] == arr[i + 1] - arr[i + 2]:
                list_chek.append("True")
            else:
                list_chek.append("False")

        if "False" in list_chek:
            return False
        else:
            return True


arr = [1, 2, 4]

s = Solution()
print(s.canMakeArithmeticProgression(arr))
