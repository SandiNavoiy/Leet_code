class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        """перестановка списка"""
        new_iter = n
        new_iter1 = int(0)
        new_list = []
        for i in range(n):
            new_list.append(nums[new_iter1])
            new_list.append(nums[new_iter])
            new_iter1 += 1
            new_iter += 1
        return new_list


nums = [1,1,2,2]
nlens = int(len(nums) / 2)

m = Solution()
x = m.shuffle(nums, nlens)
print(x)

assert x == [1,2,1,2]
