class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        """"""
        new = []
        flas = 0
        dictionary.sort()
        for i in sentence.split(" "):
            flas = 0
            for j in dictionary:
                if i[: len(j)] == j:
                    flas = 1
                    new.append(j)
                    break
            if flas == 0:
                new.append(i)
        return " ".join(new)


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"

s = Solution()
print(s.replaceWords(dictionary, sentence))
