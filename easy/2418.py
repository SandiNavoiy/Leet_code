class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        """Сортировка людей"""
        new_arr = []
        new = list(zip(names, heights))
        sorted_people = sorted(new, key=lambda x: x[1], reverse=True)
        for i in sorted_people:
            new_arr.append(i[0])
        return new_arr


names = ["Мэри", "Джон", "Эмма"]
heights = [180, 165, 170]

s = Solution()
print(s.sortPeople(names, heights))
