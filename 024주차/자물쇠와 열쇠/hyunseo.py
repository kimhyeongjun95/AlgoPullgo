# 프로그래머스 자물쇠와 열쇠

def solution(key, lock):
    N = len(lock)
    M = len(lock)
    
    def turn(place):
        new = []
        for i, j in place:
            new.append((j, M-1-i))
        return new
        
        
    lock_down = []
    flag = True
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                if flag:
                    si = i
                    sj = j
                    flag = False
                    continue
                lock_down.append((si-i, sj-j))
    
    if not lock_down:
        return True
    
    key_up = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                key_up.append((i, j))
    
    for _ in range(4):
        for ki, kj in key_up:
            temp = [(ki, kj)]
            for di, dj in lock_down:
                if (ki-di, kj-dj) not in key_up:
                    break
                temp.append((ki-di, kj-dj))
            else:
                rest_key = list(set(key_up)-set(temp))
                for ri, rj in rest_key:
                    if si-N < ki-ri <= si and sj-N < kj-rj <= sj and (ki-ri, kj-rj) not in lock_down:
                        break
                else:
                    return True
        
        key_up = turn(key_up)
    
    return False

key = [[0, 0, 0], [1, 1, 0], [0, 1, 0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))