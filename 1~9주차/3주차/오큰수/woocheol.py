# i7298번 오큰수
num = int(input())
arr = list(map(int, input().split()))


ans = [-1 for _ in range(num)]
for i in range(num-1):
    for j in range(i+1, num):
        if arr[i] < arr[j]:
            ans[i] = arr[j]
            break

print(*ans)

# naive하게 푸는 경우 시간초과를 피할 수 없다.
# 따라서 stack을 이용

ans = [-1 for _ in range(num)]
stack = []

for i in range(num-1):
    if arr[i] < arr[i+1]:
        ans[i] = arr[i+1]
        if stack:
            while stack:
                if arr[stack[-1]] < arr[i+1]:
                    ans[stack.pop()] = arr[i+1]
                else:
                    break
    else:
        stack.append(i)

print(*ans)
