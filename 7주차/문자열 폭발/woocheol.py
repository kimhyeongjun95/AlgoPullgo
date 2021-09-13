string = input()
bomb = input()

stack = []

for s in string:
    stack.append(s)
    if s == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop(-1)
ans = ''
if stack:
    ans = ''.join(stack)
else:
    ans = 'FRULA'
print(ans)
