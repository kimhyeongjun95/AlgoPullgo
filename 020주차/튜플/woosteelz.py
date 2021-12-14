# 튜플

def solution(s):
    answer = []
    temp = []
    a = ""
    for k in s:
        if k == "{" or k == "}":
            continue
        elif k == ",":
            temp.append(int(a))
            a = ""
        else:
            a += k
    if int(a):
        temp.append(int(a))

    temp_set = set(temp)
    arr2D = []
    for n in temp_set:
        arr2D.append([n, temp.count(n)])
    arr2D.sort(key=lambda x: x[1])

    for a in arr2D:
        answer.append(a[0])

    answer.reverse()

    return answer
