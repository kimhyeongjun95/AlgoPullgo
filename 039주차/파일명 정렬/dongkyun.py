def solution(files):
    answer = []
    dab = []
    for t in files:
        HEAD = ''
        NUMBER = ''
        TAIL = ''
        flag = False
        for k in range(len(t)):
            if t[k].isdigit():
                NUMBER += t[k]
                flag = True
            elif not flag:
                HEAD += t[k]
            else:
                TAIL = t[k:]
                break
        answer.append((HEAD,NUMBER,TAIL))
        
    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
    
    for dasi in answer:
        p = ''
        p = p + dasi[0] + dasi[1] + dasi[2]
        dab.append(p)

    return dab