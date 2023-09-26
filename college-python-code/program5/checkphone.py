# Write a function called isphonenumber () to recognize a pattern 415-555-4242 without using regular expression and also write the code to recognize the same pattern using regular expression.
import re


def isphonenumber(num):
    if (len(num) != 12):
        return False
    for i, val in enumerate(num):
        if ((i == 3 or i == 7)):
            if (val != "-"):
                return False
        else:
            if (val.isdigit() == False):
                return False
    return True


def chkphonenum(num):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}')
    if (pattern.match(num)):
        return True

    return False


ph_num = input("Enter a phone number: ")
no_reg = isphonenumber(ph_num)
reg = chkphonenum(ph_num)

print("without using regex")
if (no_reg):
    print(f"{ph_num} is valid")
else:
    print(f"{ph_num} is not valid")

print("using regex")
if (reg):
    print(f"{ph_num} is valid")
else:
    print(f"{ph_num} is not valid")
