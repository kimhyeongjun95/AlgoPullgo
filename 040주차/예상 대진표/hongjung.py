import math

def solution(n, a, b):
    if a > b:
        a, b = b, a

    answer = 1
    if b - a == 1 and a % 2 == 1 and b % 2 == 0:
        return answer

    while True:
        if b - a == 1 and a % 2 == 1 and b % 2 == 0:
            break
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1

    return answer

print(solution(8, 4, 6))
print(solution(8, 4, 7))