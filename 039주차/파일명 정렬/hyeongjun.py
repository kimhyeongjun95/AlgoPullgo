# 프로그래머스 (2018 카카오) 파일명 정렬

# 이름 순으로 정렬된 파일 목록은 보기 
# # 숫자를 반영한 정렬 기능을 구현하기로 했다
# 파일명은 HEAD, NUMBER, TAIL로 구성

# HEAD : 문자
# NUMBER : 숫자
# # TAIL : 나머지, null 

# 0. HEAD, NUMBER, TAIL로 구분하기
# 1. 숫자 앞에 0 없애기
# 2. HEAD 사전 순 정렬 (대소문자 구분 X)
# 3. 숫자순 정렬 (9 < 10 < 0011 < 012 < 13 < 014)
# 4. 입력순

import copy
def solution(files):
    
    answer = []
    see = []
    for file in files:
        result = []
        head = []
        rest = []
        number = []
        tail = []
        # 0
        # HEAD
        for i in range(len(file)):
            if file[i].isnumeric():
                rest.append(file[i:])
                break
            head.append(file[i])
        # NUMBER
        rest2 = []
        for i in rest:
            for j in i:
                rest2.append(j)
        for i in range(len(rest2)):
            if not rest2[i].isnumeric():
                # TAIL
                tail.append(rest2[i:])
                break
            number.append(rest2[i])

        # 1
        total = sum(map(int, number))
        if total > 0:
            value = copy.deepcopy(number)
            while value[0] == '0':
                value = value[1:]
            value = int(''.join(value))
        else:
            value = 0

        head = ''.join(head)
        head_lower = head.lower()
        number = ''.join(number)
        if tail:
            last_tail = []
            for i in tail:
                for j in i:
                    last_tail.append(j)
            tail = ''.join(last_tail)
        else:
            tail = ''
        
        result.extend((head, head_lower, number, value, tail))
        see.append(result)
    see.sort(key = lambda x: (x[1], x[3]))
    for i in see:
        temp = i[0] + i[2] + i[4]
        answer.append(temp)
    return answer

        


# print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
print(solution(["hello00000, hello0001, hello0002"]))
