# 백준 17070 파이프 옮기기 1 : dp

N = int(input())
house = [[0 for _ in range(N+1)]]
for _ in range(N):
    house.append([0] + list(map(int, input().split())))

dp = [[[0 for _ in range(3)] for _ in range(N+1)] for _ in range(N+1)]

# 0 : 가로 / 1 : 세로 / 2 : 대각선
# 첫 번째 행은 가로로만 도착할 수 있음 / 시작점 (1, 2)
for j in range(2, N+1):
    if not house[1][j]:
        dp[1][j][0] = 1

for i in range(1, N+1):
    for j in range(2, N+1):
        # 대각선
        if i+1 <= N and j+1 <=N:
            if not house[i][j+1] and not house[i+1][j] and not house[i+1][j+1]:
                dp[i+1][j+1][2] = dp[i][j][0] + dp[i][j][1] + dp[i][j][2]
        
        # 가로
        if j+1 <= N and not house[i][j+1]:
            dp[i][j+1][0] = dp[i][j][0] + dp[i][j][2]
        
        # 세로
        if i+1 <= N and not house[i+1][j]:
            dp[i+1][j][1] = dp[i][j][1] + dp[i][j][2]

answer = 0
for s in range(3):
    answer += dp[N][N][s]

print(answer)


# def push_pipe(i, j, state):
#     global cnt 

#     if i == N and j == N:
#         cnt += 1
#         return
    
#     # 대각선으로 이동
#     if i+1 <= N and j+1 <=N:
#         if not house[i][j+1] and not house[i+1][j] and not house[i+1][j+1]:
#             push_pipe(i+1, j+1, 'diagonal')
    
#     # 가로로 이동
#     if state != 'vertical':
#         if j+1 <= N and not house[i][j+1]:
#             push_pipe(i, j+1, 'horizon')
    
#     # 세로로 이동
#     if state != 'horizon':
#         if i+1 <= N and not house[i+1][j]:
#             push_pipe(i+1, j, 'vertical')


# N = int(input())
# house = [[0 for _ in range(N+1)]]
# for _ in range(N):
#     house.append([0] + list(map(int, input().split())))

# cnt = 0
# push_pipe(1, 2, 'horizon')

# print(cnt)