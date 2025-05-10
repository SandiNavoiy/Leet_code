class Solution:
    def hasSameDigits(self, s: str) -> bool:
        '''Проверьте, равны ли цифры в строке после операций I'''
        while len(s)>2:
            temp = []
            for i in range(len(s)-1):
                temp.append(str((int(s[i]) + int(s[i+1]))%10))

            s= "".join(temp)


        if s[0] == s[1]:
            return True
        else:
            return False


s = Solution()
print(s.hasSameDigits("3902"))
