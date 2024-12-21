from decimal import Decimal, ROUND_UP

def calculate_final_amount(principal, rate, years):
    principal = Decimal(principal)
    rate = Decimal(rate) / 100

    for _ in range(years):
        principal += principal * rate

    return principal.quantize(Decimal('0.0001'), rounding=ROUND_UP)

# Input reading

principal = input()
rate = input()
years = input()

final_amount = calculate_final_amount(principal, rate, int(years))
print(final_amount)
