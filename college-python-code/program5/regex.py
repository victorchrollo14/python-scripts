import re

file = open("example.txt", "r")
lines = file.readlines()

phone_pattern = re.compile(r'[+]\d{12}')
email_pattern = re.compile(r'[A-Za-z0-9_.%$]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}')

for line in lines:
    matches = phone_pattern.findall(line)
    for match in matches:
        print(match)

    matches = email_pattern.findall(line)
    for match in matches:
        print(match)
