class Solution:
    def filterRestaurants(
        self,
        restaurants: list[list[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int,
    ) -> list[int]:
        """"""
        new = []
        for restaurant in restaurants:
            if veganFriendly == 1:
                if (
                    restaurant[2] == veganFriendly
                    and restaurant[3] <= maxPrice
                    and restaurant[4] <= maxDistance
                ):
                    new.append(restaurant)
            else:
                if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                    new.append(restaurant)
        new.sort(key=lambda x: (x[1], x[0]), reverse=True)
        rez = []
        for i in new:
            rez.append(i[0])
        return rez


restaurants = [
    [1, 4, 1, 40, 10],
    [2, 8, 0, 50, 5],
    [3, 8, 1, 30, 4],
    [4, 10, 0, 10, 3],
    [5, 1, 1, 15, 1],
]
veganFriendly = 1
maxPrice = 50
maxDistance = 10
s = Solution()
print(s.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))
