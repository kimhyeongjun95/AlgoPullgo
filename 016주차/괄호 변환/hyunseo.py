# 프로그래머스 괄호 변환
def is_correct(string):
    stack = []

    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                return False
            stack.pop()
    
    if stack:
        return False
    
    return True


def solution(p):
    if is_correct(p):
        return p

    answer = ''

    def change_correct(string):
        nonlocal answer
        
        if not string:
            return string

        u = [string[0]]
        v = []

        for i in range(1, len(string)):
            if u.count('(') == u.count(')'):
                v = string[i:]
                break
            else:
                u.append(string[i])
        
        if is_correct(u):
            answer += ''.join(u)
            change_correct(''.join(v))
        else:
            answer += '('
            change_correct(''.join(v))
            answer += ')'
            for i in range(1, len(u)-1):
                if u[i] == '(':
                    answer += ')'
                else:
                    answer += '('
    
    change_correct(p)

    return answer

# print(solution('(()())()'))
# print(solution(')('))
print(solution('()))((()'))