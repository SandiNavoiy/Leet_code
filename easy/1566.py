class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        i = 0
        while i <= len(arr) - 1:
            p = arr[i : i + m]
            if p * k == arr[i : i + m * k]:
                return True

            i += 1

        return False


arr = [1, 2, 1, 2, 1, 1, 1, 3]
m = 2
k = 2
s = Solution()
print(s.containsPattern(arr, m, k))
