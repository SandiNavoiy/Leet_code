class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        ranges.sort()
        for start, end in ranges:
            if end < left:
                continue  # skip all intervals < left
            if start > left:
                return False  # don't cover diapason [left:start-1]
            if end >= right:
                return True  # diapason from left to right is covered fully
            left = end + 1

        return False


ranges = [[1, 2], [3, 4], [5, 6]]
left = 2
right = 5
s = Solution()
print(s.isCovered(ranges, left, right))
