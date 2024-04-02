class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        """"""
        count = 0
        while len(students) > count:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                x = students.pop(0)
                students.append(x)
                count += 1
        return count


students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]

s = Solution()
print(s.countStudents(students, sandwiches))
