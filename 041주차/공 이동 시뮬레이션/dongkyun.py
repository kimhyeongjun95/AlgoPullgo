def solution(n, m, x, y, queries):
    top = bottom = y
    left = right = x
    
    for direction, dx in queries:
        if direction  == 0: 
            if left != 0:
                left += dx
                if left > m - 1:
                    left = m - 1
            right += dx
            if right > m - 1:
                right = m - 1

        elif direction == 1:
            left -= dx
            if left < 0:
                left = 0
            if right != m - 1:
                right -= dx
                if right < 0:
                    right = 0

        elif direction == 2:
            if top != 0:
                top += dx
                if top > n -1:
                    top = n -1
            bottom += dx
            if bottom > n - 1:
                bottom = n - 1

        elif direction == 3:
            top -= dx
            if  top < 0:
                 top = 0
            if bottom != n -1:
                bottom -= dx
                if bottom < 0 :
                    bottom = 0

        if top > n-1 or bottom < 0 or left > m -1  or right < 0:
            return 0
    
            
    return (bottom -top + 1) * (right - left +1)