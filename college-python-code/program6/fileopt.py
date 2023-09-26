# Write a python program to accept a file name from the user and perform the following operations

# Display the first N line of the file
# Find the frequency of occurrence of the word accepted from the user in the file

from os.path import isfile
import sys

filename = input("enter filename: ")

if (not isfile(filename)):
    print(f"{filename} doesn't exist")
    sys.exit(0)

file = open(filename, "r")
lines = file.readlines()

for index, line in enumerate(lines):
    print(f"{index}: {line}")

cnt = 0
word = input("enter the word to check frequency: ")
for line in lines:
    cnt += line.count(word)

print(f"`{word}` appears {cnt} times")
