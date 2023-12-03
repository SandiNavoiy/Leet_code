class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        """"""
        x = ("1", "2", "3","4", "5", "6", "7", "8", "9", "0")
        new  = ""
        for i in word:
            if i in x:
                new = new + i
            else:
                new = new + "_"

        new_list = new.split("_")
        new_list1 = []
        for i in new_list:
            if i != "":
                new_list1.append(int(i))

        return len(list(set(new_list1)))
word = "a123bc34d8ef34"
s = Solution()
print(s.numDifferentIntegers(word))