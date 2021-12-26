def solution(n, k, cmds):
    nodes = {0: [n - 1, 1]}
    for i in range(1, n):
        if i == n - 1:
            nodes[i] = [i - 1, 0]
        else:
            nodes[i] = [i - 1, i + 1]
    
    stack = []
    for cmd in cmds:
        if len(cmd) > 1:
            c, x = cmd.split(' ')
            cnt = 0
            if c == 'D':
                while cnt < int(x):
                    k = nodes[k][1]
                    cnt += 1
            else:
                while cnt < int(x):
                    k = nodes[k][0]
                    cnt += 1
        else:
            if cmd == 'C':
                nodes[nodes[k][0]][1] = nodes[k][1]
                nodes[nodes[k][1]][0] = nodes[k][0]
                stack.append([k, nodes[k]])
                tmp = nodes[k]
                del nodes[k]
                
                if tmp[1] == 0:
                    k = tmp[0]
                else:
                    k = tmp[1]
            else:
                curr_node, val = stack.pop()
                prev_node, next_node = val
                nodes[curr_node] = [prev_node, next_node]
                nodes[prev_node][1] = curr_node
                nodes[next_node][0] = curr_node
    
    answer = ''
    for i in range(n):
        try:
            nodes[i]
            answer += 'O'
        except:
            answer += 'X'
    
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))



# def solution(n, k, cmd):
#     answer = ['O'] * n
#     delete = []
#     point = k
#     for c in cmd:
#         c = c.split(" ")
#         if c[0] == "U":
#             num = int(c[1])
#             while num > 0:
#                 point -= 1
#                 if answer[point] == 'O':
#                     num -= 1
#         elif c[0] == "D":
#             num = int(c[1])
#             while num > 0:
#                 point += 1
#                 if answer[point] == 'O':
#                     num -= 1
#         elif c[0] == "C":
#             answer[point] = 'X'
#             delete.append(point)
#             while True:
#                 point += 1
#                 flag = False
#                 if point == n:
#                     flag = True
#                     while True:
#                         point -= 1
#                         if answer[point] == 'O':
#                             break
#                 if flag:
#                     break
#                 if answer[point] == 'O':
#                     break
#         else:
#             tmp = delete.pop()
#             answer[tmp] = 'O'

#     answer = ''.join(answer)
#     return answer