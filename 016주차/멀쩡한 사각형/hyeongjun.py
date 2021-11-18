# 프로그래머스 Summer/Winter Coding(2019) 멀쩡한 사각형

# 8 x 12 = 96
# 96 - 16 = 80개 반환

# 대각선으로 직사각형을 접는다.
# 가로 길이 x 2를 빼야하나? -> X
# 2x3은 4개인데 3x3은 3개이다.
# 사용할 수 없는 사각형의 수 : (w+h-최대공약수)

def solution(w,h):
    x, y = w, h
    while y:
        z = x % y
        x, y = y, z

    return (w*h) - (w+h-x)
    # 다음부턴 math 라이브러리 쓰자(자꾸 까먹음)


print(solution(8, 12))