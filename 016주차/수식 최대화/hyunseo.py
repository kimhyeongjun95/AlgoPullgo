# 프로그래머스 수식 최대화

from itertools import permutations

def calculate(num2, num1, operator):
    if operator == '*':
        return num1*num2
    elif operator == '+':
        return num1+num2
    else:
        return num1-num2
    
    
def solution(expression):    
    answer = 0
    
    temp = ['*', '+', '-']
    # 우선 순위 정하기
    for operator in permutations(temp):
        # 우선 순위에 따라 후위 표기법으로 변경
        postfix = []
        stack = []
        num = ''
        for s in expression:
            if s.isnumeric():
                num += s
            else:
                postfix.append(int(num))
                num = ''
                
                if stack:
                    # 스택의 top보다 우선순위가 높으면 push
                    if operator.index(stack[-1]) > operator.index(s):
                        stack.append(s)
                    # 아닐경우 pop후 push
                    else:
                        while stack and operator.index(stack[-1]) <= operator.index(s):
                            postfix.append(stack.pop())
                        stack.append(s)
                # 스택이 비어있다면 연산자를 push
                else:
                    stack.append(s)

        postfix.append(int(num))

        # 스택에 남아있는 것 모두 pop
        while stack:
            postfix.append(stack.pop())
        
        # 후위표기법 계산
        stack = []
        for x in postfix:
            if type(x) == int:
                stack.append(x)
            else:
                stack.append(calculate(stack.pop(), stack.pop(), x))
        
        answer = max(answer, abs(stack[0]))
                    
    return answer

print(solution("100-200*300-500+20"))