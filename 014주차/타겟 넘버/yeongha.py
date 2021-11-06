def solution(numbers, target):
    l = len(numbers)
    ans = 0

    def dfs(n, num):
        nonlocal ans

        if num - sum(numbers[n:]) > target:
            return
        elif num + sum(numbers[n:]) < target:
            return

        if n == l:
            if num == target:
                ans += 1
            return

        dfs(n+1, num+numbers[n])
        dfs(n+1, num-numbers[n])

    dfs(0, 0)
    return ans

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
        