class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        new = []
        for word in words:
            temp_chars = list(chars)  # Создаем временную копию символов
            valid = True
            for char in word:
                if char in temp_chars:
                    temp_chars.remove(char)
                else:
                    valid = False
                    break
            if valid:
                new.append(word)
        rez = 0
        for i in new:
            rez += len(i)

        return rez


Words = ["cat", "bt", "hat", "tree"]
chars = "atach"
s = Solution()
print(s.countCharacters(Words, chars))
