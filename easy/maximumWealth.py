class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_list = []

        for i in accounts:
            sum_of_list = sum(i)
            max_list.append(sum_of_list)
        return max(max_list)


accaunts = [[1, 5], [7, 3], [3, 5]]

s = Solution()
print(s.maximumWealth(accaunts))
