class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        ''''''
        n = 0
        for i in range(len(plants)):
            if plants[i] > capacity:
                n = n + i + i+1
                capacity = 5
                capacity = capacity - plants[i]
            else:
                capacity = capacity - plants[i]
                n = n + i+1
            print(n)
        return n

plants = [2,2,3,3]
capacity = 5
s = Solution()
print(s.wateringPlants(plants, capacity))