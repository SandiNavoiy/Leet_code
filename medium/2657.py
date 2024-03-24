class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        """Finds the common"""
        new = []

        for i in range(len(A)):
            new.append(len(set(A[0 : i + 1]) & set(B[0 : i + 1])))

        return new


A = [1, 3, 2, 4]
B = [3, 1, 2, 4]
s = Solution()
print(s.findThePrefixCommonArray(A, B))
