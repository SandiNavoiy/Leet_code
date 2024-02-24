import time


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        start_time = time.time()  # Record the start time

        row = [1]
        for i in range(numRows):
            print(row)
            row = [sum(x) for x in zip([0] + row, row + [0])]

        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Execution time: {execution_time} seconds")

        return row


numRows = 5
s = Solution()
print(s.generate(numRows))
