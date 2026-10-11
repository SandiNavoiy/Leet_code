class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        """Ближайший доступный дрон."""
        ind = -1
        rass = 999999999999999999999999999999999999
        for i in range(len(drones)):
            if abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1]) <= drones[i][2]:
                if abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1]) < rass:
                    rass = abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1])
                    ind = i

        return ind



s = Solution()
print(s.nearestDrone([[2,9,3],[-25,0,15]], [-25,-15]))


