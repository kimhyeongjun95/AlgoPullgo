import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
# 좌표의 가로, 세로를 쭉 늘려서 생각
p_move = t % (w * 2)
q_move = t % (h * 2)

p_tmp = p + p_move
q_tmp = q + q_move
# 거울에 반사된 것처럼 좌표를 재설정해줌
if w < p_tmp <= w * 2:
    p_tmp = w * 2 - p_tmp

if h < q_tmp <= h * 2:
    q_tmp = h * 2 - q_tmp

# 마지막으로 범위를 넘을 수 있기 때문에 한번 더 나누어 줌
p_result = p_tmp % (w * 2)
q_result = q_tmp % (h * 2)

print(p_result, q_result)