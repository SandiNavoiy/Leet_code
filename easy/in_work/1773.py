class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        """"""


items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "lenovo"],
    ["phone", "gold", "iphone"],
]
ruleKey = "color"
ruleValue = "silver"
s = Solution()
print(s.countMatches(items, ruleKey, ruleValue))
