class Solution:
    def stringSequence(self, target: str) -> list[str]:
        ''''''
        rez = []
        for i in range(len(target)):

            for j in range(97,170):
                if chr(j) != target[i]:
                    rez.append(target[:i] +chr(j))
                elif chr(j) == target[i]:
                    rez.append(target[:i] +chr(j))
                    break
                elif chr(j) == 'z':
                    j = 97
        return rez
target = "he"

s = Solution()
print(s.stringSequence(target))

