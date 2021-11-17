def solution(w,h):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    g = gcd(w, h)
    answer = w*h -(w+h-g)
    return answer

# def solution(w,h):

#     def gcd(x, y):
#         while(y):
#             x, y = y, x % y
#         return x

#     g = gcd(w, h)
#     nw, nh = w/g, h/g
#     cnt = (nw+nh-1)

#     answer = int(w*h - (g*(nw+nh-1)))
#     return answer

w, h = 8, 12
print(solution(w, h))