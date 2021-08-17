import sys # 시간초과

N = int(sys.stdin.readline())
numbers = [0] + list(map(int, sys.stdin.readline().split())) + [0]

result = ''
for i in range(1, N+1):
    tmp = ''
    for j in range(i+1, N+2):
        if numbers[i] < numbers[j]:
            tmp = str(numbers[j])
            break
    if tmp == '':
        result += ('-1 ')
    else:
        result += (tmp + ' ')

print(result[:-1])