import sys
from collections import deque
from itertools import permutations


def solution(expression):
    answer = 0
    operand = ['+', '*', '-']
    operand = permutations(operand)
    express = []
    temp = ''
    for e in expression:
        if e == '*' or e == '+' or e == '-':
            express.append(int(temp))
            express.append(e)
            temp = ''
        else:
            temp += e
    express.append(int(temp))

    answer = []
    for o in operand:
        stack = deque(express)
        for i in range(3):
            temp_stack = deque()
            while stack:
                curr = stack.popleft()
                if curr == o[i] and curr == '*':
                    a = stack.popleft()
                    b = temp_stack.pop()
                    temp_stack.append(a * b)
                elif curr == o[i] and curr == '+':
                    a = stack.popleft()
                    b = temp_stack.pop()
                    temp_stack.append(a + b)
                elif curr == o[i] and curr == '-':
                    a = stack.popleft()
                    b = temp_stack.pop()
                    temp_stack.append(b - a)
                else:
                    temp_stack.append(curr)
            stack = temp_stack

        answer.append(abs(stack.pop()))

    return max(answer)
