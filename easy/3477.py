from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        """Фрукты в корзины II"""
        rez = len(fruits)
        flag = [0 for i in range(len(baskets))]
        for i in fruits:
            for j in range(len(baskets)):
                if i <= baskets[j] and flag[j] == 0:
                    flag[j] = 1
                    rez -= 1
                    break

        return rez


s = Solution()
print(s.numOfUnplacedFruits([4,2,5], [3,5,4]))