def getGCD(x, y):
    while y:
        x, y = y, x % y
    return x


def solution(w, h):
    answer = 1

    if w > h:
        w, h = h, w

    gcd = getGCD(w, h)

    total = w * h

    w = w // gcd
    h = h // gcd

    dum = (w + h - 1) * gcd

    answer = total - dum

    return answer
