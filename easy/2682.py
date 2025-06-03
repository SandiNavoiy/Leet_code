class Solution:
    def circularGameLosers(self, n: int, k: int) -> list[int]:
        """Найдите проигравших в круговой игреь"""

        arr = [i for i in range(1, n + 1)]
        s = set()
        i = 0
        step = 0
        while True:
            if arr[step] in s:
                return sorted(set(arr) - s)
            else:
                s.add(arr[step])
                i += 1
                step = (step + i * k) % len(arr)


s = Solution()
print(s.circularGameLosers(n=4, k=4))
