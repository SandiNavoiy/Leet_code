class Solution:
    def smallestNumber(self, num: int) -> int:
       '''Наименьшее значение переставленного числа'''
       if num> 0:
           temp = [i for i in str(num)]
           temp.sort()

           xxx = []
           while temp[0] == '0':
               xxx.append(temp.pop(0))
           if xxx:
               temp = temp[0:1] + xxx + temp[1:]


           return int("".join(temp))
       elif num < 0:
           temp = [i for i in str(num)[1:]]
           temp.sort(reverse=True)
           return int("".join(temp))*-1

       else:
          return 0


s = Solution()
print(s.smallestNumber(95005))
