import math


def solution(W, H):
    answer = (W * H) - (W + H - math.gcd(W, H))
    
    return answer