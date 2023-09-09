
def fn(n):
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fn(n - 1) + fn(n - 2)

num = int(input("Enter a number: "))
res = fn(num)
if(num > 0):
    print(f"fn({num}) is {res}", sep="")
else:
    print("Error in input")