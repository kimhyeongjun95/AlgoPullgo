while True:
    
    texts = input()
    result = []      

    if texts == '.':
        break

    for text in texts:

        if text == '(' or text == '[':
            result.append(text)

        elif text == ')':
            if result and result[-1] == '(':
                result.pop()
            else:
                result.append(text)
                break

        elif text == ']':
            if result and result[-1] == '[':
                result.pop()
            else:
                result.append(text)
                break
    
    if result:
        print('no')
    else:
        print('yes')    
