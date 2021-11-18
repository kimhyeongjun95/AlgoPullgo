# 프로그래머스 [카카오 인턴] 수식 최대화

from itertools import permutations

def calculator(poss, idx, express):

    if express.isdigit():
        return str(express)
    
    else:
        if poss[idx] == '+':
            splited = express.split('+')
            temp = []
            for s in splited:
                temp.append(calculator(poss, idx+1, s))
            return str(eval('+'.join(temp)))

        if poss[idx] == '-':
            splited = express.split('-')
            temp = []
            for s in splited:
                temp.append(calculator(poss, idx+1, s))
            return str(eval('-'.join(temp)))
        

        if poss[idx] == '*':
            splited = express.split('*')
            temp = []
            for s in splited:
                temp.append(calculator(poss, idx+1, s))
            return str(eval('*'.join(temp)))

def solution(expression):
    # 3가지의 연산문자
    # 우선순위를 재정의한다. / 동일한 순위 불가능
    # 음수라면 해당 숫자 절대값 변환
    
    answer = 0

    operator = ['+', '-', '*']
    possible = list(permutations(operator, 3))
    
    for poss in possible: # 연산자 경우의 수 돌려보기
        result = abs(int(calculator(poss, 0, expression))) # idx 0부터 시작해서 재귀로

        if result > answer:
            answer = result

    return answer
    
# 100-200*300-500+20
# * + -
print(solution("100-200*300-500+20")) # 60420
print(solution("50*6-3*2")) # 300