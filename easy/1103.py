class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        """"""
        new = [0 for i in range(num_people)]
        t = 1
        while candies > 0:
            print(new)
            for i in range(len(new)):
                if t > candies:
                    new[i] = new[i] + candies
                    candies = 0
                else:
                    new[i] = new[i] + t
                    candies = candies - t
                t = t + 1
                if candies == 0:
                    break

        return new


candies = 60
num_people = 4
s = Solution()
print(s.distributeCandies(candies, num_people))
