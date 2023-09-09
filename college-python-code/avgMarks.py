m1 = int(input("enter marks for test1: "))
m2 = int(input("enter marks for test2: "))
m3 = int(input("enter marks for test3: "))

minimum = min(m1, m2, m3)

print(minimum)
avgMarks = ((m1 + m2 + m3 - minimum)/2)

print(avgMarks)