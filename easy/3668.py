class Solution:
    def recoverOrder(self, order, friends):
        """Восстановить порядок отделки."""
        rez = []

        for i in order:
            if i in friends:
                rez.append(i)

        return rez

order = [3,1,2,5,4]
friends = [1,3,4]
s = Solution()
print(s.recoverOrder(order, friends))
