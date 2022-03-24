# 프로그래머스 뉴스 클러스터링

def multiset(string):
    temp = []
    i = 0
    while i < len(string)-1:
        if string[i].isalpha():
            if string[i+1].isalpha():
                temp.append(string[i:i+2])
            else:
                i += 1
        i += 1
    return temp
    

def solution(str1, str2):
    set_A = multiset(str1.lower())
    set_B = multiset(str2.lower())
    
    if not set_A and not set_B:
        return 65536
    
    intersection = set(set_A)&set(set_B)
    union = set(set_A)|set(set_B)
    
    multi_intersection = 0
    for word in intersection:
        multi_intersection += min(set_A.count(word), set_B.count(word))
        
    multi_union = 0
    for word in union:
        multi_union += max(set_A.count(word), set_B.count(word))
    
    return int((multi_intersection/multi_union)*65536)