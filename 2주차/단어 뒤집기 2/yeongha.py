import sys

string_list = sys.stdin.readline()
temp = False
result = ''
string = ''

for i in string_list:
    if i == '>':
        temp = False

    if temp:
        result += i
        continue

    if i.isalpha() or i.isdigit():
        string += i
    else:
        result += string[::-1]
        result += i
        string = ''

        if i == '<':
            temp = True

print(result)