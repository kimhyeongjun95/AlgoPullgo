import sys

calculation = sys.stdin.readline().rstrip()

cal_list = []
tmp = '' # 요소가 숫자인 것들을 한꺼번에 모아서 append하기 위한 임시 변수
i = 0
while True:
    if calculation[i].isdigit(): # 해당 인덱스의 요소가 숫자이면
        if i == len(calculation) - 1: # 인덱스가 끝이면
            tmp += calculation[i]
            cal_list.append(tmp)
            break
        if calculation[i+1].isdigit(): # 해당 인덱스의 다음 요소도 숫자이면
            tmp += calculation[i] # 임시 저장
            i += 1
        else: # 해당 인덱스의 다음 요소가 기호이면
            tmp += calculation[i]
            cal_list.append(tmp) # 임시 변수 append
            tmp = '' # 임시 변수 초기화
            i += 1
    else:
        cal_list.append(calculation[i]) # 해당 인덱스가 기호이면
        i += 1

result = int(cal_list[0])
minus = False # 해당 식 안에 '+'만 있을 때를 생각해서
i = 2
while i < len(cal_list): # 만약 해당 식에서 '-'가 한번이라도 나오면 그 뒤에 있는 모든 숫자는 무조건 뺄셈으로 생각함
    if cal_list[i-1] == '-':
        minus = True # 이제부터 뒤의 숫자들은 모두 빼준다
        result -= int(cal_list[i])
        i += 2
    else:
        if minus:
            result -= int(cal_list[i])
            i += 2
        else: # 아직 '-'가 나오지 않은 경우
            result += int(cal_list[i])
            i += 2

print(result)