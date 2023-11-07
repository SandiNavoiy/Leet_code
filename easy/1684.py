class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count = 0
        for word in words:
            temp = set()
            for i in word:
                temp.add(i)
            for i in temp:
                if i not in allowed:
                    break
            else:
                count += 1
        return count


allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
s = Solution()
print(s.countConsistentStrings(allowed, words))  # Вызовите метод на экземпляре класса
