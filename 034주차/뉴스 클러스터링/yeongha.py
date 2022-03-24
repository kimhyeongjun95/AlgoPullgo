from collections import defaultdict

def find(a):
    dic = defaultdict(int)
    for i in range(len(a)-1):
        element = a[i:i+2]
        if not element.isalpha():
            continue
        element = element.lower()
        dic[element] += 1
    return dic

def solution(str1, str2):

    dict1 = find(str1)
    dict2 = find(str2)

    if not dict1 and not dict2:
        return 65536

    intersection_cnt = 0
    union_cnt = 0

    for key in dict1:
        if key in dict2:
            intersection_cnt += min(dict1[key], dict2[key])
            union_cnt += max(dict1[key], dict2[key])
        else:
            union_cnt += dict1[key]

    for key in dict2:
        if not key in dict1:
            union_cnt += dict2[key]

    return int((intersection_cnt / union_cnt)*65536)
