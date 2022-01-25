# 프로그래머스 2*n 타일링

# 효율성 3개 틀림
# def solution(n):
#     tile = [0 for _ in range(n+1)]
#     tile[1] = 1
#     tile[2] = 2
    
#     for i in range(3, n+1):
#         tile[i] = tile[i-1] + tile[i-2]
    
#     return tile[n]%1000000007

def solution(n):
    tile = [0 for _ in range(n+1)]
    tile[1] = 1
    tile[2] = 2
    
    for i in range(3, n+1):
        tile[i] = (tile[i-1] + tile[i-2])%1000000007
    
    return tile[n]