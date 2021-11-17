answer = 0


def solution(numbers, target):
    dfs(numbers, 0, 0, target)
    return answer


def dfs(arr, _sum, cnt, target):
    global answer
    if cnt == len(arr) and _sum == target:
        answer += 1
        return
    if cnt == len(arr):
        return

    dfs(arr, _sum + arr[cnt], cnt+1, target)
    dfs(arr, _sum - arr[cnt], cnt+1, target)
