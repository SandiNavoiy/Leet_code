class Solution:
    def distanceBetweenBusStops(
        self, distance: list[int], start: int, destination: int
    ) -> int:
        n = len(distance)
        if start > destination:
            start, destination = destination, start
        distance = distance + distance
        dist1 = sum(distance[start:destination])
        dist2 = sum(distance[destination : start + n])
        return min(dist1, dist2)


distance = [
    6,
    47,
    48,
    31,
    10,
    27,
    46,
    33,
    52,
    33,
    38,
    25,
    32,
    45,
    36,
    3,
    0,
    33,
    22,
    53,
    8,
    13,
    18,
    1,
    44,
    41,
    14,
    5,
    38,
    25,
    48,
]
start = 22
destination = 0
s = Solution()
print(s.distanceBetweenBusStops(distance, start, destination))
