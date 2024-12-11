code = input()
n = int(input())
if (code == "sq" or code == "tr") and 1 <= n <= 9:
    if code == "sq":
        for i in range(n):
            print("#"*2*n)
    else:
        for i in range(n):
            print(" "*(n-i) + "#"*(2*i+1))
else:
    print("WRONG_DATA")