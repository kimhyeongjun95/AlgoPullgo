def solution(n):
    def dfs(queen, row):
        count = 0
        if n == row:
            return 1
        for col in range(n):
            queen[row] = col
            for i in range(row):
                if queen[i] == queen[row]:
                    break
                if abs(queen[i]-queen[row]) == row - i:
                    break
            else:
                count += dfs(queen, row + 1)
        return count
        
    return dfs([0] * n, 0)

print(solution(4))