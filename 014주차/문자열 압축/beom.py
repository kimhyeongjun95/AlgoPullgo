def solution(s):
    answer = 0
    result = []
    
    if len(s) == 1:
        return 1

    # 절반만 압축
    for i in range(1, len(s)//2 + 1): # i = 1, 2, 3, 4
        compress = ""
        cnt = 1
        temp = s[:i]

        # 1개 문자열부터 반복 검증
        for j in range(i, len(s), i):  # 1, 8, 1  / j = 1 2 3 4 5 6 7
            if s[j:i+j] == temp:
                cnt += 1
            else:
                # 반복과 다른 값을 만났을 때
                if cnt == 1:
                    compress += temp
                    temp = s[j:i+j]
                else:
                    compress += str(cnt) + temp
                    temp = s[j:i+j]
                    cnt = 1

        # 마지막까지 같은 경우를 검증하기 위함
        if cnt == 1:
            compress += temp
        else:
            compress += str(cnt) + temp
        result.append(len(compress))
    
    answer = min(result)

    return answer