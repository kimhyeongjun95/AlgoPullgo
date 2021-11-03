def solution(s):
    if len(s) == 1:
        return 1
    
    answer = 1000
    for i in range(1, len(s)//2+1):
        temp = []
        for j in range(0, len(s), i):
            temp.append(s[j:j+i])
        
        temp_result = 0
        overlap = 0
        for j in range(len(temp)-1):
            if temp[j] != temp[j+1]:
                if overlap:
                    temp_result += i
                    temp_result += len(str(overlap+1))
                    overlap = 0
                else:
                    temp_result += i
            else:
                overlap += 1
        
        if overlap:
            temp_result += i
            temp_result += len(str(overlap))
        else:
            temp_result += len(temp[-1])
            
        if answer > temp_result:
            answer = temp_result
            
    return answer