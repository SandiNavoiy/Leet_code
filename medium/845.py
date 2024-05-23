class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        """"""
        n = len(arr)
        if n < 3:
            return 0
        max_length = 0
        for i in range(1, n - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                left = i - 1
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1

                right = i + 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                current_length = right - left + 1
                max_length = max(max_length, current_length)

        return max_length


arr = [[2, 2, 2]]
s = Solution()
print(s.longestMountain(arr))
