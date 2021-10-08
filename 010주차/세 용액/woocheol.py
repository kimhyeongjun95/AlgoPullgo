# 2473번 세 용액
N = int(input())
arr = list(map(int, input().split()))
ans = [0, 0, 0]
flag = False
arr.sort()

sum3 = float('inf')
for i in range(N-2):
    left, right = i+1, N-1
    while left < right:
        temp = arr[i] + arr[left] + arr[right]

        if sum3 > abs(temp):
            sum3 = abs(temp)
            ans[0] = arr[i]
            ans[1] = arr[left]
            ans[2] = arr[right]

        if temp == 0:
            flag = True
            break

        if temp > 0:
            right -= 1
        else:
            left += 1
    if flag:
        break

print(*ans)
