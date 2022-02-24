# 프로그래머스 N-Queen

def solution(n):
    cols = set()
    minus = set()
    plus = set()
    
    answer = 0
    def queen(row):
        nonlocal n, answer
        
        if row == n:
            answer += 1
            return
        
        for col in range(n):
            if col not in cols and row-col not in minus and row+col not in plus:
                cols.add(col)
                minus.add(row-col)
                plus.add(row+col)
                
                queen(row+1)
                
                cols.remove(col)
                minus.remove(row-col)
                plus.remove(row+col)
    
    queen(0)
    
    return answer