n = int(input())
stack = []
for _ in range(n):
    temp = int(input())
    if temp:
        stack.append(temp)
    else:
        stack.pop(-1)

print(sum(stack))
