def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for word in words:
        if word in s:
            s = s.replace(word, str(words.index(word)))
            
    return int(s)