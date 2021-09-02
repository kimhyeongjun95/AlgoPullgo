# 동근이는 X에 위치

# 1번 상점
# 시계 방향 : 12
# 반 시계방향 : 18
# 최단거리는 12

# 블록의 크기 / 상점의 개수와 위치 / 동근이의 위치 given
# 최단 거리의 합

# 1 : 북쪽 / 2 : 남쪽 / 3 : 서쪽 / 4 : 동쪽
# 2번째 입력은 : 1,2는 왼쪽 경계 3,4는 위쪽 경계
# 마지막은 동근이의 위치

    # 시계 방향 갈때 다른 direction에 위치한다면
    # 북쪽 : far +
    # 동쪽 : far +
    # 남쪽 : far +
    # 서쪽 : far +

    # 반시계 방향 다른 direction에 위치한다면
    # 북쪽 : width - far
    # 동쪽 : height - far 
    # 남쪽 : width - far
    # 서쪽 : height - far

    # 1. 같은 direction에 위치한지 확인한다.
    # 1-1. 같은 direct: far가 큰지? current_far가 큰지?
    #       큰거에서 빼주기 -> 무조건 최단값
    # 1-2. 다른 direction:
        # anti / clock에서 작은값 더하기
        # 처음 시작은 위에 인용

    # 왼쪽에서는 far 더해주고
    # 오른쪽에서는 width - far해주고
    # 어떤 숫자가 더 작은지 확인

    # 위에서는 far 더해주고
    # 아래에서는 height - far

def path_finder(stores):
    clock_path = 0 # 시계 방향
    anti_path = 0 # 반시계 방향
    temp = 0 # 같은 direction 용
    answer = []
    while stores:
        direction, far = stores.pop() # 1, 4
        
        if direction == current_direction: # 같은 줄에 있다면
            if far > current_far: # 큰 숫자에서 작은 숫자 빼기
                answer.append(far-current_far)
            else:
                answer.append(current_far-far)

        else: # 다른 direction이면
            if direction == 1: # 북쪽이고
                if current_direction == 3: # 서쪽이라면 // 무조건 시계방향이 빠름.
                    clock_path = current_far + far
                    answer.append(clock_path)
                elif  current_direction == 4: # 동쪽이라면 // 무조건 반시계방향이 빠름.
                    anti_path = current_far + (width - far)
                    answer.append(anti_path)
                elif current_direction == 2: # 남쪽이라면 // 비교
                    clock_path = far + height + current_far
                    anti_path = (width-far) + height + (width-current_far)
                    if clock_path > anti_path:
                        answer.append(anti_path)
                    else:
                        answer.append(clock_path)
            
            elif direction == 2: # 남쪽이고
                if current_direction == 1: # 북쪽이라면 // 비교
                    anti_path = far + height + current_far
                    clock_path = (width - current_far) + height + (width - far)
                    if clock_path > anti_path:
                        answer.append(anti_path)
                    else:
                        answer.append(clock_path)
                elif current_direction == 3: # 서쪽이라면 // 반시계 방향이 빠름.
                    anti_path = current_far + (width - far)
                    answer.append(anti_path)
                elif current_direction == 4: # 동쪽이라면 // 시계방향이 빠름.
                    clock_path = current_far + far
                    answer.append(clock_path)

            ######################################### 서쪽/동쪽 과 남쪽/북쪽의 공식이 약간 다름.
            
            elif direction == 3: # 서쪽이고
                if current_direction == 1: # 북쪽이라면 // 반시계 방향이 빠름.
                    anti_path = current_far + far
                    answer.append(anti_path)
                elif current_direction == 2: # 남쪽이라면 // 시계방향이 빠름.
                    clock_path = current_far + (height - far)
                    answer.append(clock_path)
                elif current_direction == 4: # 동쪽이라면 // 비교
                    anti_path = current_far + width + far
                    clock_path = (height-current_far) + width + (height-far)
                    if clock_path > anti_path:
                        answer.append(anti_path)
                    else:
                        answer.append(clock_path)
            
            elif direction == 4: # 동쪽이고
                if current_direction == 1: # 북쪽이라면 // 시계방향이 빠름
                    clock_path = (width-current_far) + far
                    answer.append(clock_path)
                elif current_direction == 2: # 남쪽이라면 / 반시계 방향이 빠름.
                    anti_path = (width-current_far) + (height-far)
                    answer.append(anti_path)
                elif current_direction == 3: # 서쪽이라면 // 비교
                    clock_path = current_far + width + far
                    anti_path = (height-current_far) + width + (height-far)
                    if clock_path > anti_path:
                        answer.append(anti_path)
                    else:
                        answer.append(clock_path)
    
    return answer


width, height = map(int, input().split())
n = int(input())

stores = [] # 상점 위치
for _ in range(n):
    direction, far = map(int, input().split())
    stores.append((direction, far))

current_direction, current_far = map(int, input().split()) # 현재 위치

answer = sum(path_finder(stores)) # 함수 사용 [5, 6, 12]
print(answer)

'''
10 5
3
1 4
3 2
2 8
2 3
'''