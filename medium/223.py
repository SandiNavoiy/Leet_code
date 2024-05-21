class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        """"""

        new_x1 = max(ax1, bx1)
        new_x2 = min(ax2, bx2)
        new_y1 = max(ay1, by1)
        new_y2 = min(ay2, by2)

        return (
            (abs(ax1 - ax2) * abs(ay1 - ay2))
            + (abs(bx1 - bx2) * abs(by1 - by2))
            - (abs(new_x1 - new_x2) * abs(new_y1 - new_y2))
        )


ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2

s = Solution()
print(s.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
