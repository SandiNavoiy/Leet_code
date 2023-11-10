class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        arr=[]
        res=[]
        for i in range(m):
            arr.append(i+1)

        for i in range(len(queries)):
            ind=arr.index(queries[i])
            arr.pop(ind)
            res.append(ind)
            arr.insert(0,queries[i])
        return res
queries = [7,5,5,8,3]
m = 8

s = Solution()
print(s.processQueries(queries,m))