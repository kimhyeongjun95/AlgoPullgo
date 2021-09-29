import sys

def save_profit(num):
    global profits
    if num > N:
        return
    if num + schedule[num][0] <= N + 1:
        for i in range(num+schedule[num][0], N+2):
            profits[num][i] = (profits[num-1][num] + schedule[num][1])
    for j in range(1, N+2):
        profits[num][j] = max(profits[num-1][j], profits[num][j])
    save_profit(num+1)
        

N = int(sys.stdin.readline())
schedule = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
profits = [[0] * (N+2) for _ in range(N+1)]

save_profit(1)
max_num = 0
for i in range(N+1):
    for j in range(N+2):
        if profits[i][j] > max_num:
            max_num = profits[i][j]

print(max_num)






# import sys

# N = int(sys.stdin.readline())
# schedule = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# profit = 0
# for i in range(1, N+1):
#     d = i
#     temp = 0
#     while True:
#         if d + schedule[d][0] <= N + 1:
#             temp += schedule[d][1]
#             if d + schedule[d][0] < N + 1:
#                 d += schedule[d][0]
#             else:
#                 break
#         else:
#             break
#     if temp > profit:
#         profit = temp

# print(profit)