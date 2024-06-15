class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        """"""
        new_arr = [i for i in arr]
        new_arr.sort()

        n = len(arr) - 1
        rez = []
        max_c = max(arr)

        while new_arr != arr:
            if arr.index(max_c) == 0:
                arr = arr[::-1]
                rez.append(n + 1)

            elif arr.index(max_c) == n:
                t = arr[0:n]
                arr = t[::-1] + [arr[-1]]
                rez.append(n)
            elif arr.index(max_c) == n - 1:
                arr = arr[::-1]
                rez.append(n + 1)
            else:
                t = arr[0 : arr.index(max_c) + 1]
                rez.append(arr.index(max_c) + 1)

                arr = t[::-1] + arr[arr.index(max_c) + 1 :]

        return rez


arr = [3, 2, 4, 1]
s = Solution()
print(s.pancakeSort(arr))
