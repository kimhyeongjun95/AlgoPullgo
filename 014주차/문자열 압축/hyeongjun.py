# 프로그래머스 카카오 기출 문자열압축 
def solution(s):
    # // 2 : 최대 반까지만 압축 가능
    result = len(s) # 결과로 쓰일 압축 길이의 최소값
    for number in range(1, (len(s)//2)+1): # 1개 부터 확인
        total = ''
        temp = s[:number]
        count = 1
        
        for j in range(number, len(s), number):
            if temp == s[j:j+number]:
                count += 1
            else:
                if count >= 2:
                    total += str(count) + temp
                else:
                    total += temp

                temp = s[j:j+number]
                count = 1
        
        # 마지막 문자열 처리
        if count >= 2:
            total += str(count) + temp
        else:
            total += temp
        
        result = min(result, len(total))
    
    return result




print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))