# 프로그래머스 숫자 문자열과 영단어

from collections import deque

def solution(s):
    def str_to_int(string):
        number = {
            'zero' : '0', 'one' : '1', 'two' : '2',
            'three' : '3', 'four' : '4', 'five' : '5',
            'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'
        }
        
        numbers = []
        while len(string) > 5:
            if string[:3] in number.keys():
                numbers.append(number[string[:3]])
                string = string[3:]
            elif string[:4] in number.keys():
                numbers.append(number[string[:4]])
                string = string[4:]
            elif string[:5] in number.keys():
                numbers.append(number[string[:5]])
                string = string[5:]
        
        numbers.append(number[string])
            
        return deque(numbers)
    
    
    answer = ''
    temp = ''
    for word in s:
        if word.isnumeric():
            if temp:
                queue = str_to_int(temp)
                while queue:
                    answer += queue.popleft()
                temp = ''
            
            answer += str(word)
        else:
            temp += word
    
    if temp:
        queue = str_to_int(temp)
        while queue:
            answer += queue.popleft()
            
    return int(answer)