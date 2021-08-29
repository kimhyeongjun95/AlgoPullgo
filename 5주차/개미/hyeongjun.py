import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 왼쪽 아래 0, 0
# 오른쪽 위가 w, h
# p, q 개미 위치 /  1시간 후 (p+1, q+1)
# 출력 : t 시간 후 개미의 위치 좌표

# 2차원행렬...? 안만들어도 되겠다.
# 1. w과 h크기의 숫자 limit
# 2. x과 y에 대한 flag
# 2-1. 각각 w과 h가 그리고 0과 0이 될때마다 증감 조절
# 3. count가 t가 될때까지 반복

# count = 0
# flag_p = True
# flag_q = True
# while count < t:
#     if flag_p:
#         p += 1
#     else:
#         p -= 1

#     if flag_q:
#         q += 1
#     else:
#         q -= 1

#     if p == w:
#         flag_p = False
#     elif p == 0:
#         flag_p = True

#     if q == h:
#         flag_q = False
#     elif q == 0:
#         flag_q = True

#     count += 1

# t가 최대 2억..
# 점화식으로 풀면? 델타처럼 만들어주면????
p_move = []
q_move = []

for i in range(w+1):
    p_move.append(i)
for i in range(w-1, 0, -1): # 길이 이상으로 넘어가면 바로 반사하도록
    p_move.append(i)
for i in range(h+1):
    q_move.append(i)
for i in range(h-1, 0, -1):
    q_move.append(i)

p = p_move[(p+t) % len(p_move)] 
q = q_move[(q+t) % len(q_move)] # 한번만 연산해주면 되니까..?
print(p, q)