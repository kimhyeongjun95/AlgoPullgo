# 효율성 테스트 성공 못함
def solution(n, works):

    while n > 0:
        works[works.index(max(works))] -= 1
        if sum(works) == 0:
            break
        n -= 1
        
    answer = 0
    for w in works:
        answer += w**2
    return answer


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))