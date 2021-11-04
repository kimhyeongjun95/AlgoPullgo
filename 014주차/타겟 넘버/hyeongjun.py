# 프로그래머스 LV 2 : 타겟 넘버
def solution(numbers, target):
    length = len(numbers)
    answer = 0
    
    # 지금이 몇번째인지 세는 용도의 숫자와, 처음 배열의 숫자가 양수와 음수일 때
    stack = [(0, numbers[0]), (0, -(numbers[0]))]
    while stack:
        idx, total = stack.pop()
        
        if idx == length-1: # 배열을 모두 돌았으면
            if total == target: # 만약 경우의 수가 target이라면
                answer += 1
        else:
            stack.append((idx+1, total+numbers[idx+1]))
            stack.append((idx+1, total-numbers[idx+1]))
    
    return answer



print(solution([1, 1, 1, 1, 1], 3))