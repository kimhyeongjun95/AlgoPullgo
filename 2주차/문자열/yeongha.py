import sys

A, B = sys.stdin.readline().split()
B_list = list(B)

min_result = len(A)
for i in range(len(B)-len(A)+1):
    result = 0
    for j in range(1, len(A)+1):
        if A[-j]!=B_list[-j]:
            result += 1
    if min_result > result:
        min_result = result
    B_list.pop()

print(min_result)