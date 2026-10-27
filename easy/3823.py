class Solution:
    def reverseByType(self, s: str) -> str:
        """"""

        boova = []
        spec = []

        for char in s:
            if char.isalpha():
                boova.append(char)
            else:
                spec.append(char)

        boova = boova[::-1]
        spec = spec[::-1]


        rez = []

        for char in s:
            if char.isalpha():
                rez.append(boova.pop(0))
            else:
                rez.append(spec.pop(0))

        return "".join(rez)
s = Solution()
print(s.reverseByType(" )ebc#da@f( "))