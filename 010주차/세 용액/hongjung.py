import sys # 시간초과

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

result = sum(numbers[:3])
i = 0
j = 1
k = 2
start = i
mid = j
end = k
while start < N - 2:
    if result == 0:
        break
    if (result > 0) and (numbers[i] + numbers[j] + numbers[k] > 0):
        if numbers[i] + numbers[j] + numbers[k] > result:
            break
    elif (result < numbers[i] + numbers[j] + numbers[k] <= 0) or (0 <= numbers[i] + numbers[j] + numbers[k] < result):
        result = numbers[i] + numbers[j] + numbers[k]
        start = i
        mid = j
        end = k
        if i == N - 3:
            break
        if j == N - 2:
            i += 1
            j = i + 1
            k = j + 1
        else:
            k += 1
            if k == N:
                j += 1
                k = j + 1
    else:
        if i == N - 3:
            break
        if j == N - 2:
            i += 1
            j = i + 1
            k = j + 1
        else:
            k += 1
            if k == N:
                j += 1
                k = j + 1

print(numbers[start], numbers[mid], numbers[end])
