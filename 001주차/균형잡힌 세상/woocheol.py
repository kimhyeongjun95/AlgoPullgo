# 4949번 균형잡힌 세상
from collections import deque

while True:
    sentence = input()
    stack = deque()

    if sentence == '.':
        break

    for word in sentence:
        if word == '[':
            stack.append(']')
        elif word == '(':
            stack.append(')')
        elif word == ')' or word == ']':
            if stack and stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
                print('no')
                break

    else:
        if stack:
            print('no')
        else:
            print('yes')
