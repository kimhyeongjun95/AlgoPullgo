# 백준 14888 연산자 끼워넣기
from itertools import permutations

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num1 >= 0 :
            return num1//num2
        else:
            return -((-num1)//num2)


N = int(input())
numbers = list(map(int, input().split()))
temp = list(map(int, input().split()))
operator = ['+', '-', '*', '/']
operators = []

for i in range(4):
    for _ in range(temp[i]):
        operators.append(operator[i])

results = []
for opers in set(permutations(operators)):
    result = numbers[0]
    for i in range(N-1):
        result = calculate(result, numbers[i+1], opers[i])
    
    results.append(result)

print(max(results))
print(min(results))