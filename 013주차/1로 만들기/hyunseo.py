# 백준 1463 1로 만들기

def making_one(num, cnt):
    global min_cnt

    if num <= 0 or cnt >= min_cnt:
        return

    if num == 1:
        min_cnt = min(min_cnt, cnt)
        return

    if not num%3:
        making_one(num//3, cnt+1)
    
    if not num%2:
        making_one(num//2, cnt+1)

    making_one(num-1, cnt+1)


N = int(input())

min_cnt = float('inf')
making_one(N, 0)

print(min_cnt)