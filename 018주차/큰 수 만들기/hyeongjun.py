# 프로그래머스 큰 수 만들기

def solution(number, k):
    stack = []
    for i in number:
        # if가 아니라 while로 해야 큰 수 가능
        while stack and stack[-1] < i and k:
            k -= 1
            stack.pop()
        stack.append(i)
    
    return ''.join(stack[:len(stack)-k])
    return ''.join(stack)
    # 히든 테스트 케이스 : k가 남은 경우
    # '54321'



print(solution('1924', 2)) # '94'
print(solution('1231234', 3)) # '3234'
print(solution('4177252841', 4)) # '775841'