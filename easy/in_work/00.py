from datetime import datetime, timedelta
n= input()
dt = datetime.strptime(n, '%d-%m-%Y')
dt = dt.date()
print('Payment Schedule:')
for i in range(12):

    print(f"Payment {i+1}: {dt.strftime('%Y-%d-%m-%Y')}")
    dt = dt + timedelta(days=28)



