class Solution:
    def countBits(self, n: int) -> list[int]:
        ''''''
        new_list = [x for x in range(n+1)]
        result = []
        for i in new_list:
            ind = format(i, 'b')
            rem = list(ind)
            x = []
            for j in rem:
                x.append(int(j))
            y = sum(x)
            result.append(y)

        return result

n = 5
s = Solution()
print(s.countBits(n))
#[0,1,1,2,1,2]