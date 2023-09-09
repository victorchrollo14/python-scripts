class Pali:
    def __init__(self):
        self.isPali = False

    def chkPalindrome(self, value):
        if str(value) == str(value)[::-1]:
            self.isPali = True
        else:
            self.isPali = False

        return self.isPali


class PaliInt(Pali):
    def chkPalindrome(self, val):
        str_val = str(val)
        if str_val == str_val[::-1]:
            self.isPali = True
        else:
            self.isPali = False

        return self.isPali


st = input("Enter a string : ")
stObj = Pali()

if stObj.chkPalindrome(st):
    print("Given string is a Palindrome")
else:
    print("Given string is not a Palindrome")

val = int(input("Enter an integer : "))
intObj = PaliInt()

if intObj.chkPalindrome(val):
    print("Given integer is a Palindrome")
else:
    print("Given integer is not a Palindrome")


