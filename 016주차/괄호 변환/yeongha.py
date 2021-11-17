def balanced(p):
    new = []
    for i in p:
        if i == '(':
            new.append('(')
        else:
            if not new:
                return False
            else:
                new.pop()
    if new:
        return False
    else:
        return True

answer = ''
def solution(p):
    global answer
    if not p or balanced(p):
        answer += p
    else:
        # p = list(p)
        open_cnt = close_cnt = 0
        i = 0
        for i in range(len(p)):
            if p[i] == '(':
                open_cnt += 1
            else:
                close_cnt += 1
            if open_cnt == close_cnt:
                break
            
        u, v = p[:i+1], p[i+1:]
        if balanced(u):
            answer += u
            solution(v)
        else:
            answer += '('
            solution(v)
            answer += ')'
            for i in u[1:len(u)-1]:
                if i == '(':
                    answer += ')'
                else:
                    answer += '('
    return answer


p = "()))((()"
print(solution(p))