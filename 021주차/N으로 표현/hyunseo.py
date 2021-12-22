# 프로그래머스 N으로 표현

def solution(N, number):
    answer = -1
    all_cases = [{}]
    
    for i in range(1, 9):
        temp = set()
        # N을 i번 사용하는 경우
        temp.add(int(str(N)*i))
        
        for j in range(1, i):
            for a in all_cases[j]:
                for b in all_cases[i-j]:
                    temp.add(a+b)
                    temp.add(a-b)
                    temp.add(a*b)
                    if b:
                        temp.add(a//b)
        
        if number in temp:
            answer = i
            break
        
        all_cases.append(temp)

    return answer 