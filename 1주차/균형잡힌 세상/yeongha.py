import sys

def balanced_world(string):
    result = []
    output = "yes"
    for i in string:
        if i == '(':
            result.append(i)
        elif i == '[':
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

input_string = sys.stdin.readline()
print(balanced_world(input_string))