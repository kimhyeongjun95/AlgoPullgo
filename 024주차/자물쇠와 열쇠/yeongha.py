def rotate(M, spins):
    new_spins = []
    l = len(spins)
    for x, y in spins:
        new_spins.append((y, M-x-1))
    return new_spins

def move_x(M, spins, m):
    new_spins = []
    l = len(spins)
    for x, y in spins:
        new_spins.append((x+m, y))
    return new_spins

def move_y(M, spins, m):
    new_spins = []
    l = len(spins)
    for x, y in spins:
        new_spins.append((x, y+m))
    return new_spins

def find_key(N, M, spins, holes, lock):
    new_holes = holes[:]
    for x, y in spins:
        if 0 <= x-(M-1) < N and 0 <= y-(M-1) < N:
            if lock[x-(M-1)][y-(M-1)] == 1:
                return False
            else:
                new_holes.remove((x, y))
    if not new_holes:
        return True
    return False

def solution(key, lock):
    spins = []
    holes = []
    N, M = len(lock), len(key)

    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                spins.append((i,j))

    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                holes.append((i+M-1,j+M-1))
    

    for i in range(N+2*M-5):
        new_spins = move_y(M, spins, i)
        for j in range(N+2*M-5):
            new_new_spins = move_x(M, new_spins, j)
            if find_key(N, M, new_new_spins, holes, lock):
                return True

    for i in range(3):
        spins = rotate(M,spins)
        for i in range(N+2*M-5):
            new_spins = move_y(M, spins, i)
            for j in range(N+2*M-5):
                new_new_spins =  move_x(M, new_spins, j)
                if find_key(N, M, new_new_spins, holes, lock):
                    return True
    
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))