import sys

S = list(map(str, sys.stdin.readline().rstrip()))

i = 0
while True:
    # '<>'를 '()'로 바꿈. 왜냐하면, index 메서드로 '<>'를 앞에서부터 찾기 때문에 일단 '()'로 바꿔주고 나중에 다시 '<>'로 변경
    if S[i] == '<':
        S[i] = '('
        i = S.index('>')
        S[i] = ')'
        i += 1 # 인덱스를 '>' 다음으로 바꿔줌
        if i == len(S): # '>' 다음이 없으면 즉, 리스트의 길이와 동일하다면 반복문 종료
            break
    elif S[i] == ' ': # 해당 인덱스의 문자가 공백이면 인덱스를 하나 증가시켜줌
        i += 1
    else:
        tmp_str = [] # 거꾸로 된 문자열을 만들어주기 위한 임시 리스트
        tmp = 0 # 인덱스 i의 문자열부터 언제까지의 문자열을 선택할 것인지 범위를 설정하기 위한 임시 변수
        for j in range(i, len(S)):
            # '<'도 아니고 공백도 아니면 문자열을 임시 리스트에 추가하고, 그게 아니면 바로 for 반복문 종료
            if S[j] != '<' and S[j] != ' ':
                tmp_str.append(S[j])
                tmp += 1
            else:
                break
        S[i:i+tmp] = tmp_str[::-1] # 리스트의 특정 구간을 거꾸로 변경시킴
        if i + tmp == len(S): # 인덱스 i와 범위를 더한 것이 전체 리스트의 길이면 반복문 종료
            break
        i = i + tmp # 인덱스의 위치를 변경한 문자열 다음의 인덱스부터 시작할 수 있도록 재설정
        
result = ''.join(S)
result = result.replace('(', '<')
result = result.replace(')', '>') # '()'를 '<>'로 다시 바꿔줌 
print(result)