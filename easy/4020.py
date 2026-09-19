class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        """Запросы на лифт I"""
        rez = 0
        for i in range(0, len(requests)-1):
            rez += abs(requests[i+1] - requests[i])




        return  rez + requests[0]


n = 5
requests = [2,1,4,3]

s = Solution()
print(s.elevatorRequests(n, requests))



