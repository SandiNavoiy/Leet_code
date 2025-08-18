class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """Игра в прыжки"""
        # длинна списка минус 1, считаем что на первую ступень мы и так прыгнули
        l = len(nums) - 1

        # перебираем возможности пшышков, в обратном направлении
        for i in range(len(nums) - 2, -1, -1):
            # если позиция + дальнрость прыжка позволяют прыгать до предыдущей
            if nums[i] + i >= l:
                l = i

        # если допрыгали то 0
        if l == 0:
            return True
        else:
            return False


s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))
