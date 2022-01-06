# 프로그래머스 숫자 문자열과 영단어
def solution(s):
    answer = ''
    temp = ''
    translate = {
        'zero':'0',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    for i in s:
        if i.isnumeric():
            answer += str(i)
        else:
            temp += i
        
        if temp in translate:
            answer += translate[temp]
            temp = ''
            
    return int(answer)
        
print(solution("one4seveneight")) 
# 1478