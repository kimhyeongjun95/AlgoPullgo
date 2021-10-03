import sys

def func(input) :
    open = []

    for word in input :
        if word == '(' or word == '[' :
            open.append(word)
        elif word == ')' :
            if not open or open[-1] != '(':
                return 'no'
            else :
                open = open[:-1]
        elif word == ']' :
            if not open or open[-1] != '[':
                return 'no'
            else :
                open = open[:-1]

    if not open :
        return 'yes'
    else :
        return 'no'

while True :
    input = sys.stdin.readline().rstrip()

    if input == '.' :
        break