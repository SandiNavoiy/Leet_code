class Solution:
    def countSeniors(self, details: list[str]) -> int:
        """Количество пожилых людей"""
        senior = 0
        for i in details:
            if int(int(i[11] + i[12])) > 60:
                senior += 1
        return senior


Details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
s = Solution()
print(s.countSeniors(Details))
