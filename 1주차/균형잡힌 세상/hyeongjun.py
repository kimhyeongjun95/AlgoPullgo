while True:
    s = input()
    counts = []
    if s[0] == '.':
        break

    for i in s:
        # number += 1
        # print(number)
        # print(counts)
        if i =='.':
            break
        if i == '(' or i == '[':
            counts.append(i)
        if i == ')' or i == ']':
            if len(counts) == 0:
                # print('no')
                counts.append(i)
            
            if counts[-1] == '(' and i == ')':
                counts.pop()
                continue
            
            if counts[-1] == '[' and i == ']':
                counts.pop()
                continue
            if counts[-1] == '[' and i == ')':
                # print('no')
                counts.append(i)
            
            if counts[-1] == '(' and i == ']':
                # print('no')
                counts.append(i)

    if len(counts) == 0:
        print('yes')
    else:
        print('no')
