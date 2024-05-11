# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    bad = 4
    if version == bad:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """"""
        start = 0
        end = n
        while start < end:
            middle = (start + end) // 2
            if isBadVersion(middle) == True:
                end = middle
            else:
                start = middle + 1
        return start


n = 5
bad = 4
s = Solution()
print(s.firstBadVersion(n))
