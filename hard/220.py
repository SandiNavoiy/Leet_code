class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: list[int], indexDiff: int, valueDiff: int
    ) -> bool:
        """"""

        if indexDiff <= 0 or valueDiff < 0:
            return False
        bucket = {}
        width = valueDiff + 1

        for i, value in enumerate(nums):
            id = value // width
            if id in bucket:
                return True
            if id - 1 in bucket and abs(value - bucket[id - 1]) < width:
                return True
            if id + 1 in bucket and abs(value - bucket[id + 1]) < width:
                return True
            bucket[id] = value
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // width]
        return False


nums = [1, 2, 3, 1]
indexDiff = 3
valueDiff = 0
s = Solution()
print(s.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))
