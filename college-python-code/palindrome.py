value = int(input("Enter a value: "))

str_val = str(value)

if(str_val == str_val[::-1]):
    print(f"{value} is a palindrome number")
else:
    print(f"{value} is not a palindrome number")

for i in range(10):
    if str_val.count(str(i)) > 0:
        print(str(i),"appears", str_val.count(str(i)), "times")

    

