# 14888번 연산자 끼워넣기

N = int(input())
nums = list(map(int, input().split()))
operation = list(map(int, input().split()))
ans_max = float('-inf')
ans_min = float('inf')


def calculate(idx, total, operation):
    global ans_max, ans_min

    if idx == N:
        ans_max = max(ans_max, total)
        ans_min = min(ans_min, total)
        return

    for i in range(4):
        if operation[i]:
            operation[i] -= 1
            if i == 0:
                calculate(idx+1, total + nums[idx], operation)
            if i == 1:
                calculate(idx+1, total - nums[idx], operation)
            if i == 2:
                calculate(idx+1, total * nums[idx], operation)
            if i == 3:
                calculate(idx+1, int(total / nums[idx]), operation)
            operation[i] += 1


calculate(1, nums[0], operation)
print(ans_max)
print(ans_min)
