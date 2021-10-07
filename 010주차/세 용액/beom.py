import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
min_val = float('inf')

for i in range(N-2):
    start = i + 1
    end = N - 1

    while start < end:
        sum_val = arr[i] + arr[start] + arr[end]
        if abs(sum_val) <= min_val:   
            min_val = abs(sum_val)
            result = [arr[i], arr[start], arr[end]]
        if sum_val < 0:
            start += 1
        elif sum_val > 0:
            end -= 1
        else:
            break
            
print(*result)