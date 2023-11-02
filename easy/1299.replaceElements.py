class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        """Замените элементы наибольшим элементом справа"""
        new_list = []
        for i in range(len(arr)):

            if i < len(arr) - 1:
                new_list.append(max(arr[i + 1:(len(arr))]))
            else:
                new_list.append(-1)
        return new_list
arr = [17,18,5,4,6,1]
#[18,6,6,6,1,-1]
s = Solution()
print(s.replaceElements(arr))