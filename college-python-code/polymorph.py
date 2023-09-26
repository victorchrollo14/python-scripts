class Pali:
    def __init__(self):
        self.isPali = False

    def chkPalindrome(self, strVal):
        if (strVal == strVal[::-1]):
            self.isPali = True

        return self.isPali


class PaliInt(Pali):
    def chkPalindrome(self, intVal):
        intVal = str(intVal)
        rev = intVal[::-1]
        if (intVal == rev):
            self.isPali = True
        else:
            self.isPali = False

        return self.isPali


input1 = input("Enter a string: ")
strObj = Pali()
if (strObj.chkPalindrome(input1)):
    print(f"{input1} is a palindrome")
else:
    print(f"{input1} is not a palindrome")

input2 = int(input("Enter an integer: "))
intObj = PaliInt()

if (intObj.chkPalindrome(input2)):
    print(f"{input2} is a palindrome")
else:
    print(f"{input2} is not a palindrome")
