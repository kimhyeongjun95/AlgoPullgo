def solution(p):

    switch = {'(': ')', ')': '('}

    while True:
        
        # 빈 문자열 반환
        if len(p) == 0:
            return p
 
        # u,v로 분리
        u, v = divide_uv(p)
 
        # 3단계
        if checked(u):
            
        # 3-1
            return u + solution(v)
 
        # 4단계
        else:

            # 4-1 ~ 4-3단계
            answer = '(' + solution(v) + ')'

            # 4-4단계
            u = u[1:-1]
            for i in u:
                answer += switch[i]

            return answer


def checked(u):
    stack = []
    
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    return True  
 
 
def divide_uv(p):
    
    weight = {'(': 1, ')': -1}
    weight_total = 0

    for i in range(len(p)):
        weight_total += weight[p[i]]
        if weight_total == 0:
            break
 
    u = p[:i + 1]
    v = p[i + 1:]
 
    return u, v