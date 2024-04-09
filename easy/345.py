class Solution:
    def reverseVowels(self, s: str) -> str:
        """"""
        glass = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        nn = []
        for i in s:
            if i in glass:
                nn.append(i)
        nn = nn[::-1]
        print(nn)

        new_str_arr = [x for x in s]

        for i in range(len(new_str_arr)):
            if new_str_arr[i] in glass:
                new_str_arr[i] = nn[0]
                nn.pop(0)
        return "".join(new_str_arr)


s = "aA"
sol = Solution()
print(sol.reverseVowels(s))
