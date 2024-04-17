class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        """"""

        new = list(set(list1) & set(list2))

        ind = list1.index(new[0]) + list2.index(new[0])
        x = [new[0]]
        for i in new:
            temp = list1.index(i) + list2.index(i)
            if temp < ind:
                ind = temp
                x.clear()
                x.append(i)
            elif temp == ind:
                if i not in x:
                    x.append(i)

        return x


list1 = ["happy", "sad", "good"]
list2 = ["sad", "happy", "good"]
s = Solution()
print(s.findRestaurant(list1, list2))
