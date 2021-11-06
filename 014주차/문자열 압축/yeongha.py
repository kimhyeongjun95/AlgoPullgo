def solution(s):
    answer = 1000
    if len(s) == 1:
        return 1

    for n in range(1, len(s)//2+1):
        new = ''
        temp = s[:n]
        cnt = 1
        for i in range(n, len(s), n):
            if temp == s[i:i+n]:
                cnt += 1
            else:
                if cnt == 1:
                    new += temp
                else:
                    new += str(cnt) + temp
                temp = s[i:i+n]
                cnt = 1
        
        if cnt == 1:
            new += temp
        else:
            new += str(cnt) + temp
        answer = min(answer, len(new))

    return answer

s = "xababcdcdababcdcd"
print(solution(s))