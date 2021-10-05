import sys

k = int(sys.stdin.readline())

result = []
for i in range(k):
    number = int(sys.stdin.readline())
    if number == 0:
        result.pop()
    else:
        result.append(number)

print(sum(result))