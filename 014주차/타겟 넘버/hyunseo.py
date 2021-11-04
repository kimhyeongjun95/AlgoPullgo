# 프로그래머스 타겟 넘버

def solution(numbers, target):
    temp = [[] for _ in range(len(numbers)+1)]
    temp[0].append(0)

    for i in range(len(numbers)):
        for num in temp[i]:
            temp[i+1].append(num-numbers[i])
            temp[i+1].append(num+numbers[i])
    
    answer = temp[-1].count(target)
    return answer

print(solution([1, 1, 1, 1, 1], 3), 5)
print(solution([1, 2, 1, 2], 2), 3)
print(solution([1, 2, 1, 2], 6), 1)