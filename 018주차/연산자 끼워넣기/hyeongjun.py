# 백준 14888 연산자 끼워넣기

# n개의 수로 이루어진 수열과 n-1개의 연산자
# 최대값 최소값 출력

n = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

min_result = float('inf')
max_result = float('-inf')

#dfs로 탐색
def dfs(i, now):
    global min_result, max_result, plus, minus, mul, div

    if i == n:
        min_result = min(min_result, now)
        max_result = max(max_result, now)

    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, now+numbers[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, now-numbers[i])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, now/numbers[i])
            div += 1

dfs(1, numbers[0])

print(max_result)
print(min_result)