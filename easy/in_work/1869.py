class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ''''''
        col_1 = 0
        col_0 = 0
        temp_0 = 0
        temp_1 = 0

        for i in s:

            if i == "0":
                if temp_1> col_1:
                    col_1 =  temp_1
                temp_1 = 0
                temp_0 = temp_0 + 1
            else:
                if temp_0 > col_0:
                    col_0 = temp_0
                temp_0 = 0
                temp_1 = temp_1 + 1
        col_1 = temp_1
        col_0 = temp_0
        print(col_1)
        print(col_0)

        if col_0 < col_1:
            return True
        return False
s = "111000"
sol = Solution()
print(sol.checkZeroOnes(s))