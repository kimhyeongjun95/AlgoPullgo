import sys
input = sys.stdin.readline


N = int(input())
result = 0
 
# def move(y,x,mode):
#     global result
#     if y == N-1 and x == N-1:
#         result += 1
#         return
 
#     if mode == 1:
#         if x == N-1:
#             return
 
#         if table[y][x+1] == 0:
#             move(y,x+1,1)
#             if table[y+1][x+1] == 0 and table[y+1][x] == 0:
#                 move(y+1,x+1,2)
#             return
 
table = []
for i in range(N):
    arr = list(map(int, input().split()))
    table.append(arr)
 
move(0,1,1)
print(result)