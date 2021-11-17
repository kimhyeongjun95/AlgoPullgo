def is_complete(p):
    if not p:
        return True
    arr = []
    for i in p:
        if i == ")":
            if not arr:
                return False
            else:
                arr.pop(0)
        else:
            arr.append(i)
    if arr:
        return False
    else:
        return True


def divide(p):
    openP = 0
    closeP = 0

    for i in range(len(p)):
        if p[i] == '(':
            openP += 1
        else:
            closeP += 1
        if openP == closeP:
            return p[:i + 1], p[i + 1:]


def solution(p):
    answer = ""
    if is_complete(p) or not p:
        return p
    else:
        u, v = divide(p)
        if is_complete(u):
            return u + solution(v)
        else:
            answer += "("
            answer += solution(v)
            answer += ")"

            u = list(u[1:-1])
            for i in range(len(u)):
                if u[i] == ")":
                    u[i] = "("
                else:
                    u[i] = ")"
            answer += "".join(u)

    return answer
