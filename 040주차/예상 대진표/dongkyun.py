def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a = (a+1) // 2 
        b = (b+1) // 2
        

    return answer

print(solution(8, 4, 6))
print(solution(8, 4, 7))