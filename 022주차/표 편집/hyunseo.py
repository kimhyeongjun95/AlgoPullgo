# 프로그래머스 표 편집

def solution(n, k, cmd):
    table = {x : [x-1, x+1] for x in range(n)}
    answer = ['O' for _ in range(n)]
    deleted = []
    
    for c in cmd:
        if len(c) > 1:
            c, x = c.split()
        
        if c == 'U':
            for _ in range(int(x)):
                k = table[k][0]
        elif c == 'D':
            for _ in range(int(x)):
                k = table[k][1]
        elif c == 'C':
            before, after = table[k]
            deleted.append((before, after, k))
            answer[k] = 'X'
            
            if before == -1:
                table[after][0] = before
                k = after
            elif after == n:
                table[before][1] = after
                k = before
            else:
                table[before][1] = after
                table[after][0] = before
                k = after
        elif c == 'Z':
            before, after, num = deleted.pop()
            answer[num] = 'O'
            
            if before == -1:
                table[after][0] = num
            elif after == n:
                table[before][1] = num
            else:
                table[before][1] = num
                table[after][0] = num
            
    return ''.join(answer)