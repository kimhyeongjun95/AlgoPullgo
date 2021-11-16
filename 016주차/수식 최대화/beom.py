from itertools import permutations 


def oper(num1, num2, operator):
    if operator == '+':
        return str(int(num1) + int(num2))

    if operator == '-':
        return str(int(num1) - int(num2))

    if operator == '*':
        return str(int(num1) * int(num2))


def calculate(expression, operator):
    cal_temp = []
    for i in expression:
        
        # 연산자가 아니라면
        if not i in operator:
            if len(cal_temp) != 0 and not cal_temp[-1] in operator:
                cal_temp[-1] = cal_temp[-1] + i
            else:
                cal_temp.append(i)
        # 연산자라면
        else:
            cal_temp.append(i)

    result = []
    stack = []
    for i in operator:
        while True:
            if len(cal_temp) == 0:
                break
            temp = cal_temp.pop(0)
            # 연산자라면
            if temp == i:
                stack.append(oper(stack.pop(-1), cal_temp.pop(0), i))
            # 연산자가 아니라면
            else:
                stack.append(temp)
        result.append(stack)
        cal_temp = stack
        stack = []
            
    return result[-1]


def solution(expression):
    operator = ['+', '-', '*']
    operator = list(permutations(operator, 3))
    answer = 0

    for i in operator:
        answer = max(answer, abs(int(calculate(expression, i)[0])))

    return answer