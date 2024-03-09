import time


class Solution:

    def checkPerfectNumber(self, num: int) -> bool:
        divisors_sum = 0
        for x in range(1, num):
            if num % x == 0:
                divisors_sum += x
        return divisors_sum == num

# Замеряем время выполнения кода
start_time = time.time()

num = 99999992
solution = Solution()
result = solution.checkPerfectNumber(num)

end_time = time.time()
execution_time = end_time - start_time

print(f"Result: {result}")
print(f"Execution Time: {execution_time} seconds")
