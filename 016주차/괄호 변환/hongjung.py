def divide(p):
    open = 0
    close = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            open += 1
        else:
            close += 1
        if open == close:
            return p[:i+1], p[i+1:]
 
 
def is_balance(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return True
 
 
def solution(p):
    if p == '':
        return ''
    
    u, v = divide(p)
    
    if is_balance(u):
        return u + solution(v)
    else:
        result = '('
        result += solution(v)
        result += ')'

        for i in u[1:len(u) - 1]:
            if i == '(':
                result += ')'
            else:
                result += '('

        return result


print(solution('))(('))
print(solution("(()())()"))
print(solution("()"))
print(solution("()))((()"))