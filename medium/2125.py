class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        """"""
        t = 0
        new = []
        for i in range(0, len(bank)):
            if bank[i].count("1") > 0:
                new.append(bank[i])
        for i in range(0, len(new) - 1):
            t = t + (new[i].count("1") * new[i + 1].count("1"))

        return t


bank = ["011001", "000000", "010100", "001000"]
s = Solution()
print(s.numberOfBeams(bank))
