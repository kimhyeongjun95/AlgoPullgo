def solution(n, k, cmd):

    def down(x, pointer):
        for _ in range(x):
            pointer = dict[pointer][1]
        return pointer

    def up(x, pointer):
        for _ in range(x):
            pointer = dict[pointer][0]
        return pointer

    def delete(pointer):
        nonlocal z_box
        a, b = dict[pointer]
        z_box.append([pointer, [a,b]])
        answer[pointer] = 'X'
        
        if a != -1:
            dict[a][1] = b

        if b != n:
            dict[b][0] = a
            pointer = dict[pointer][1]
        else:
            pointer = dict[pointer][0]

        return pointer


    answer = ['O'] * n
    dict = {}
    for i in range(n):
        dict[i] = [i-1, i+1]
    z_box = []
    for c in cmd:
        c = c.split()
        if c[0] == "D":
            k = down(int(c[1]), k)
        if c[0] == "U":
            k = up(int(c[1]), k)
        if c[0] == "C":
            k = delete(k)
        if c[0] == "Z":
            p, lst = z_box.pop()
            answer[p] = 'O'

            if lst[0] == -1:
                dict[lst[1]][0] = p
            elif lst[1] == n:
                dict[lst[0]][1] = p
            else:
                dict[lst[0]][1] = p
                dict[lst[1]][0] = p
        
        print(k)
        print(dict)

    return ''.join(answer)

n = 8
k = 2
cmd =["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))