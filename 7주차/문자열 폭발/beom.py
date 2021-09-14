# arr = input()
# target = input()

# while target in arr:
#     arr = arr.replace(target, '')
# if arr:
#     print(arr)
# else:
#     print('FRULA')


arr = list(input())
target = list(input())
stack = []

for i in arr:
    stack.append(i)

    if len(stack) >= len(target):
        if stack[-len(target):] == target:
            for _ in range(len(target)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
 