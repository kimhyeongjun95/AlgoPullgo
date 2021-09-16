import sys
input = sys.stdin.readline

N, K = map(int, input().split())  
num_list = [i for i in range(2, N+1)]
stack = []

while num_list:
    num = num_list.pop(0)
    stack.append(num)

    i = num
    while i <= N:
        if i in num_list:
            num_list.remove(i)
            stack.append(i)
        i += num
print(stack[K-1])