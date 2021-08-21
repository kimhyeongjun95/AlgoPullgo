#stack 이용
import sys

def nge(N, numbers):
    answer = [-1]*N
    stack = [0]
    i = 1
    while i < N:
        n = numbers[i]
        while stack and numbers[stack[-1]] < n:
            answer[stack.pop()] = n
        stack.append(i)
        i += 1
    return answer

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
print(*nge(N, numbers))
