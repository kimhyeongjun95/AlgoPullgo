# 프로그래머스 파일명 정렬

def solution(files):
    answer = []
    for i, file in enumerate(files):
        head = ''
        number = ''
        
        for f in file:
            if f.isdecimal(): # 정확하게 int로 변환가능한 것만 판별
                number += f
            else:
                if number:
                    break
                    
                head += f
        
        answer.append([file, head.lower(), int(number), i])
    
    answer.sort(key = lambda x: (x[1], x[2], x[3]))
        
    return list(x[0] for x in answer)