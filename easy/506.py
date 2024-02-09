
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        ''''''
        resuil = []
        new = sorted(score, reverse=True)
        for i in range(len(score)):
            resuil.append(str(new.index(score[i])+1))
        for j in range(len(resuil)):
            if resuil[j] == "1":
                resuil[j] = "Gold Medal"
            elif resuil[j] == "2":
                resuil[j] = "Silver Medal"
            elif resuil[j] == "3":
                resuil[j] = "Bronze Medal"

        return resuil



score = [10,3,8,9,4]
s = Solution()
print(s.findRelativeRanks(score))