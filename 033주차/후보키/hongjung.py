from collections import defaultdict
from itertools import combinations

def solution(relation):
    answer = 0
    length = len(relation)
    col_length = len(relation[0])
    r_dict = defaultdict(list)
    for i in range(length):
        for j in range(col_length):
            r_dict[j].append(relation[i][j])

    key_list = []
    check_list = list(range(col_length))
    for i in range(col_length):
        flag = True
        for j in r_dict[i]:
            if r_dict[i].count(j) >= 2:
                flag = False
                break
        if flag:
            check_list.remove(i)
            answer += 1

    for i in range(2, len(check_list) + 1):
        com = list(combinations(check_list, i))
        for c in com:
            tmp_list = []
            for j in range(length):
                tmp = []
                for k in c:
                    tmp.append(relation[j][k])
                tmp_list.append(tmp)
            
            flag = True
            for t in tmp_list:
                if tmp_list.count(t) >= 2:
                    flag = False
                    break
            
            if flag:
                if key_list:
                    for k in key_list:
                        cnt = 0
                        for l in c:
                            for m in k:
                                if l == m:
                                    cnt += 1

                        if cnt == len(k):
                            break
                    else:
                        key_list.append(c)
                else:
                    key_list.append(c)

    answer += len(key_list)
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))