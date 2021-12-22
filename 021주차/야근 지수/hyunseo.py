# 프로그래머스 야근 지수

from collections import defaultdict

def solution(n, works):
    works_dict = defaultdict(int)
    for work in works:
        works_dict[work] += 1
        
    max_num = max(works_dict.keys())
    for _ in range(n):
        works_dict[max_num] -= 1
        works_dict[max_num-1] += 1
        
        if works_dict[max_num] == 0:
            del works_dict[max_num]
            max_num = max(works_dict.keys())
        
        if max_num == 0:
            break
            
    answer = 0
    for work, cnt in works_dict.items():
        if work <= 0 :
            continue
        
        for _ in range(cnt):
            answer += work**2
            
    return answer