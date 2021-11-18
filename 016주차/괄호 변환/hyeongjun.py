# 프로그래머스 2020 KAKAO BLIND RECRUITMENT 괄호 변환

    # 균형잡힌 괄호 문자열: (의 개수와 )의 개수가 같다
    # 올바른 괄호 문자열: 짝이 모두 맞다.
    
    # 균형잡힌 괄호 문자열이 주어짐.
    # 균형잡힌 괄호 문자열 -> 올바른 괄호 문자열
    # 1. 빈 문자열, '' 반환
    # 2. u, v로 분리
    #     u: 균형잡힌 괄호 문자열로 더이상 분리 x
    #     v: 빈 문자열이 될 수 있음.
    # 3. if u == '올바른 괄호 문자열', v를 1단계부터 다시 수행
    #     3-1. 수행한 결과를 u에 이어 붙인후 반환
    # 4. elif u != '올바른 괄호 문자열':
    #     4-1. 빈 문자열에 첫번째 문자로 '('를 이어붙임.
    #     4-2. v에 대해 1단계부터 재귀적으로 수행한결과 이어붙임.
    #     4-3. ')'를 다시 붙임.
    #     4-4. u의 첫번째와 마지막 문자 제거, 나머지 문자열 괄호 방향 뒤집어서 뒤에 붙임
    #     4-5. 반환

def balance_idx(p):
    count = 0 # '('의 개수

    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def balance_checker(p):
    count = 0 # '('의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 올바른 괄호 문자열이 아니라면
                return False
            count -= 1
    return True # 올바른 괄호라면

def solution(p):
    answer = ''
    if p == '':
        return answer
    
    idx = balance_idx(p) # u(올바른 괄호 문자열)의 길이를 찾기위한 함수
    u = p[:idx+1]
    v = p[idx+1:]
    
    if balance_checker(u): # u가 올바른 괄호문자열이라면
        answer = u + solution(v)
    else: # 아니라면
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫번째와 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u) # 문자열로 바꿔서 더해주고
    return answer
    



print(solution("(()())()")) # "(()())()"
print(solution(")(")) # "()"
print(solution("()))((()")) # "()(())()"