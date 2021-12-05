import sys

N = int(sys.stdin.readline())

max_dp = [0] * 3
min_dp = [0] * 3

tmp_max_dp = [0] * 3
tmp_min_dp = [0] * 3
for i in range(N):
    row_zero, row_one, row_two = map(int, sys.stdin.readline().split())

    for j in range(3):
        if j == 0:
            tmp_max_dp[0] = row_zero + max(max_dp[0], max_dp[1])
            tmp_min_dp[0] = row_zero + min(min_dp[0], min_dp[1])
        elif j == 1:
            tmp_max_dp[1] = row_one + max(max_dp[0], max_dp[1], max_dp[2])
            tmp_min_dp[1] = row_one + min(min_dp[0], min_dp[1], min_dp[2])
        else:
            tmp_max_dp[2] = row_two + max(max_dp[1], max_dp[2])
            tmp_min_dp[2] = row_two + min(min_dp[1], min_dp[2])
    
    for j in range(3):
        max_dp[j] = tmp_max_dp[j]
        min_dp[j] = tmp_min_dp[j]

print(max(max_dp), min(min_dp))


# import sys

# def make_scores(line_idx, row_idx, plus_num):
#     global lines, max_result, min_result
#     if line_idx == N:
#         if plus_num > max_result:
#             max_result = plus_num
#         if plus_num < min_result:
#             min_result = plus_num
#         return
    
#     if plus_num > min_result and plus_num + 9 * (N - line_idx) < max_result:
#         return
    
#     if row_idx == 0:
#         make_scores(line_idx + 1, 0, plus_num + lines[line_idx][0])
#         make_scores(line_idx + 1, 1, plus_num + lines[line_idx][1])
#     elif row_idx == 1:
#         make_scores(line_idx + 1, 0, plus_num + lines[line_idx][0])
#         make_scores(line_idx + 1, 1, plus_num + lines[line_idx][1])
#         make_scores(line_idx + 1, 2, plus_num + lines[line_idx][2])
#     else:
#         make_scores(line_idx + 1, 1, plus_num + lines[line_idx][1])
#         make_scores(line_idx + 1, 2, plus_num + lines[line_idx][2])


# N = int(sys.stdin.readline())
# lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# min_result = float('inf')
# max_result = float('-inf')

# for i in range(3):
#     make_scores(0, i, 0)

# print(max_result, min_result)
