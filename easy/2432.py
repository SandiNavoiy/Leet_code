class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        '''Сотрудник, который работал над самой долгой задачей'''
        longist_time = 0
        start_work = 0
        index_longest = 0

        for i in logs:
            if longist_time < i[1] -start_work:
                longist_time = i[1] -start_work
                index_longest= i[0]
            elif longist_time == i[1] -start_work:
                if i[0] < index_longest:
                    index_longest = i[0]
            start_work = i[1]
        return  index_longest








s=Solution()
print(s.hardestWorker(10, [[0,3],[2,5],[0,9],[1,15]]))