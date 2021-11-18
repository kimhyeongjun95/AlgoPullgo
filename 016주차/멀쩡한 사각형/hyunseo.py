# 프로그래머스 멀쩡한 사각형

def solution(w,h):
    small = min(w, h)

    for n in range(small, 0, -1):
        if not w%n and not h%n:
            gcd = n
            break
    
    print(gcd)
    
    return w*h - (w+h-gcd)

# import math

# def solution(w, h):
#     return w*h - (w+h-math.gcd(w,h))

solution(1071, 1029)