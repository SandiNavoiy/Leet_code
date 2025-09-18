class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        '''Самое большое число '''
        #превращаем масив с цифры
        temp = [str(i) for i in nums]
        #сортируем массив, лексографически учитывая что 3 должго быть больше 30. поэтому дополняем число 10 раз мамим собой и сравниваем
        temp.sort(key=lambda x: x*10, reverse=True)
        #если первый символ равен 0, то возвращаем 0
        if temp[0] == "0":
            return "0"


        return "".join(temp)

s = Solution()
print(s.largestNumber([3,30,34,5,9]))

#"9 5 34 3 30"