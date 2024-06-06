class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        """"""
        people.sort(key=lambda x: (-x[0], x[1]))
        rez = []
        print(people)
        for person in people:
            rez.insert(person[1], person)

        return rez


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
s = Solution()
print(s.reconstructQueue(people))
# [[5,0], [7,0],[5,2],[6,1],[4,4],[7,1]]
