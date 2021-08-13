n,m = map(int,input().split())
r,c,d = map(int,input().split())
area = []   
for _ in range(n):
    area.append(list(map(int,input().split())))
dr = [-1,0,1,0]  # 북동남서    
dc = [0,1,0,-1]
# r,c = r-1,c-1     
area[r][c] = 2 # 2로 현재 위치가 청소가 되었음을 표시한다 2차원배열 인덱스 맞춰줘야한다
count = 1 # 답 
turn_time = 0
 
# def turn_left():
#     global d
#     d = (d - 1) % 4

while True: # 시뮬레이션 문제다!!! dfs가 아니라 재귀적으로 할 필요가 없지
    d = (d-1) % 4 # 왼쪽으로 회전
    nr = r + dr[d]
    nc = c + dc[d]
    if area[nr][nc] == 0: # 왼쪽방향이 청소가 안된 공간이라면
        r,c = nr,nc # 빈공간이면 이동한다
        area[nr][nc] = 2
        count += 1
        turn_time = 0
        continue
    else:                      # continue를 사용할 필요가 없는 경우가 있다
        turn_time += 1
    if turn_time == 4:  # if 를 중첩해서 많이쓰기 보다는 따로 조건을 쓰는게 가독성이 좋다
        nr = r - dr[d]
        nc = c - dc[d]
        if area[nr][nc] == 1:
            break
        else:
            r,c = nr,nc
            turn_time = 0
print(count)