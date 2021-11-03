def solution(numbers, target):
    def dfs(idx, n):
        nonlocal answer
        
        if idx == len(numbers):
            if n == target:
                answer += 1
            return
        
        dfs(idx+1, n+numbers[idx])
        dfs(idx+1, n-numbers[idx])
        
    answer = 0
    dfs(0, 0)
    return answer