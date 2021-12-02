import sys
input = sys.stdin.readline


def cal(a, b, op):
    if op == 0: 
        return a + b
    elif op == 1: 
        return a - b
    elif op == 2: 
        return a * b
    elif op == 3:
        if a < 0 and b > 0: 
            return - (abs(a) // b)
        else: 
            return a // b


def solution(idx, result):
    global max_result, min_result
    if idx == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    else:
        for i in range(4):
            if oper[i] != 0:
                oper[i] -= 1
                solution(idx + 1, cal(result, num_arr[idx], i))
                oper[i] += 1


N = int(input())
num_arr = list(map(int, input().split()))
oper = list(map(int, input().split()))
max_result = float('-inf')
min_result = float('inf')

solution(1, num_arr[0])
print(max_result)
print(min_result)