import sys
input = sys.stdin.readline
text = input()
result = ''
tag = ''

for i in text:
    
    if i == '<':
        result += tag
        tag = '<'
    
    elif i == '>':
        result += (tag + '>')
        tag = ''

    else:
        result = i + result
print(result)


    