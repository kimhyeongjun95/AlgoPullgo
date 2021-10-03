import sys

sentence = [] # 입력된 문장들을 저장하는 리스트
while True:
    s = sys.stdin.readline().rstrip()
    if s == '.': # '.'이 나오면 문장 입력 종료
        break
    sentence.append(s)

result = ''
for words in sentence: # 문장들을 하나씩 반복
    if words.strip() == '.': # 공백을 제거한 문장이 '.'이면 yes
        result = 'yes'
    elif words[-1] != '.': # 문장의 끝이 '.'이 아니면 no
        result = 'no'
    else:
        bracket = '' # 괄호를 입력하기 위한 변수
        for i in words:
            if i == '(' or i == ')' or i == '[' or i == ']':
                bracket += i # 괄호를 순차적으로 저장

        for j in range(len(bracket)//2): # 괄호 // 2가 짝 괄호의 최대 개수 이므로
            bracket = bracket.replace('()', '') # '()'을 공백으로 바꿈
            bracket = bracket.replace('[]', '') # '[]'을 공백으로 바꿈
    
        if bracket: # 비어있지 않으면 no
            result = 'no'
        else: # 비어있으면 yes
            result = 'yes'
    print(result)