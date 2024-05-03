class Solution:
    def findLHS(self, nums: list[int]) -> int:
        result = 0
        count_map = {}
        for num in nums:
            if num not in count_map:
                count_map[num] = 1
            else:
                count_map[num] += 1
        for num, count in count_map.items():
            if num + 1 in count_map:
                result = max(count + count_map[num + 1], result)
        return result