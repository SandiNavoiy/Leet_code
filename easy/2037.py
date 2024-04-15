class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        ''''''
        sss = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            sss = sss + abs(students[i] - seats[i])

        return sss

seats = [3,1,5]
students = [2,7,4]
s = Solution()
print(s.minMovesToSeat(seats, students))