import sys

def balanced_world(string):
    result = []
    output = "yes"
    for i in string:
        if i == '(' or i == '[':
            result.append(i)
        elif i == ')':
            if result and result[-1]=='(':
                result.pop()
            else:
                output = "no"
                return output
        elif i == ']':
            if result and result[-1]=='[':
                result.pop()
            else:
                output = "no"
                return output
    if result:
        output = 'no'
    return output

while True:
    input_string = sys.stdin.readline().rstrip()
    if input_string == '.':
        break
    print(balanced_world(input_string))