class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        tax = 0.0
        last_stage = 0
        for i in range(len(brackets)):
            if income > brackets[i][0] - last_stage:
                money = brackets[i][0] - last_stage
                income -= money
                last_stage = brackets[i][0]
                tax += money * (brackets[i][1] / 100)
            else:
                money = income
                tax += money * (brackets[i][1] / 100)
                break
        return tax


brackets = [[3, 50], [7, 10], [12, 25]]
income = 10
s = Solution()
print(s.calculateTax(brackets, income))
