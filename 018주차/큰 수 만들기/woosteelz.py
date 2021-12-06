# 프로그래머스 타겟넘버(level 2)
answer = 0


def solution(numbers, target):
    dfs(numbers, 0, 0, target)
    return answer


def dfs(arr, total, cnt, target):
    global answer
    if cnt == len(arr) and total == target:
        answer += 1
        return
    if cnt == len(arr):
        return

    dfs(arr, total + arr[cnt], cnt+1, target)
    dfs(arr, total - arr[cnt], cnt+1, target)
