def solution(w, h):
    min_num = min(w, h)
    max_num = max(w, h)

    while True:
        remainder = max_num % min_num
        if remainder == 0:
            return w * h - (w + h - min_num)
        max_num = min_num
        min_num = remainder

print(solution(8, 12))
print(solution(2, 4))