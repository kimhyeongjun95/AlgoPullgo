def solution(number, k):
    new = []
    idx = -1
    while k < len(number):
        m = '0'
        for i in range(idx+1,k+1):
            if m < number[i]:
                idx = i
                m = number[i]
                if m == '9': 
                    break

        new.append(m)
        k += 1
        
    return "".join(map(str,new))