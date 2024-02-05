class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        """"""
        new = 0
        if ruleKey == "color":
            for i in items:
                if i[1] == ruleValue:
                    new += 1

        elif ruleKey == "type":
            for i in items:
                if i[0] == ruleValue:
                    new += 1
        elif ruleKey == "name":
            for i in items:
                if i[2] == ruleValue:
                    new += 1
        return new


items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "lenovo"],
    ["phone", "gold", "iphone"],
]
ruleKey = "color"
ruleValue = "silver"
s = Solution()
print(s.countMatches(items, ruleKey, ruleValue))
