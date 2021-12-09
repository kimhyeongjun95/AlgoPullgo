import sys
input = sys.stdin.readline

N = int(input())
score = [list(map(int,input().split())) for _ in range(N)]

max_score1, max_score2, max_score3 = score[0][0],score[0][1],score[0][2]
min_score1, min_score2, min_score3 = score[0][0],score[0][1],score[0][2]

for i in range(1,N):
    max_score1, max_score2, max_score3 = max(max_score1,max_score2) + score[i][0], max(max_score1,max_score2,max_score3) + score[i][1], max(max_score2,max_score3) + score[i][2]
    min_score1, min_score2, min_score3 = min(min_score1, min_score2) + score[i][0], min(min_score1, min_score2, min_score3) + score[i][1], min(min_score2, min_score3) + score[i][2]

print(max(max_score1, max_score2, max_score3), min(min_score1, min_score2, min_score3))