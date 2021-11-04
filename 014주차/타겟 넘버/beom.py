def solution(numbers, target):
    result = [0]
    
    for i in numbers:
        temp = []
        
        for j in result:
            temp.append(j+i)
            temp.append(j-i)
        result = temp
    
    answer = result.count(target)
    return answer