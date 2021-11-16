def solution(expression):
    cases = [{'*': 1, '+': 2, '-': 3}, {'*': 1, '+': 3, '-': 2}, {'*': 2, '+': 1, '-': 3},
             {'*': 2, '+': 3, '-': 1}, {'*': 3, '+': 1, '-': 2}, {'*': 3, '+': 2, '-': 1},
            ]
    
    answer = 0
    for case in cases:
        num = ''
        to_postfix = []
        operator = []
        for e in expression:
            if e.isdigit():
                num += e
            else:
                to_postfix.append(int(num))
                num = ''
                if operator:
                    while case[e] <= case[operator[-1]]:
                        to_postfix.append(operator.pop())
                        if len(operator) == 0:
                            break
                    operator.append(e)
                else:
                    operator.append(e)

        to_postfix.append(int(num))
        while operator:
            to_postfix.append(operator.pop())
        

        temp_list = []
        for i in to_postfix:
            if type(i) == type(1):
                temp_list.append(i)
            else:
                if i == '*':
                    temp_list.append(temp_list.pop() * temp_list.pop())
                elif i == '+':
                    temp_list.append(temp_list.pop() + temp_list.pop())
                else:
                    temp_list.append(-(temp_list.pop() - temp_list.pop()))

        if abs(temp_list[0]) > answer:
            answer = abs(temp_list[0])
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))