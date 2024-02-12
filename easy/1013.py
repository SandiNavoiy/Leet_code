class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        N = len(arr)
        total = sum(arr)
        if total % 3 != 0:
            return False
        part_sum = total // 3
        to_add = part_sum
        seen = 0
        parts = 0
        for n in arr:
            seen += n
            if seen == part_sum:
                parts += 1
                part_sum += to_add
        return seen == total and parts >= 3


arr = [14,6,-10,2,18,-7,-4,11]

s = Solution()
print(s.canThreePartsEqualSum(arr))