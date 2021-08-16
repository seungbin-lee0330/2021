# 어려운 문제 다시풀기

n,m = map(int,input().split())
r,c,d = map(int,input().split())
area = []   
for _ in range(n):
    area.append(list(map(int,input().split())))
dr = [-1,0,1,0]  # 북동남서    
dc = [0,1,0,-1]    
area[r][c] = 2 # 2로 현재 위치가 청소가 되었음을 표시한다 2차원배열 인덱스 맞춰줘야한다
count = 1 # 답 
turn_time = 0
 
# def turn_left():
#     global d
#     d = (d - 1) % 4

while True: # 시뮬레이션 문제다!!! dfs가 아니라 재귀적으로 할 필요없지 언제까지 할지 모른다 while
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






n,m = map(int,input().split())
a,b,d = map(int,input().split())
maps = []
visited =[[0] * m for _ in range(n)] # 방문한 위치를 저장하기 위한 2차원 배열 초기화
visited[a][b] = 1 
for i in range(n):
    maps.append(list(map(int,input().split())))
da = [-1,0,1,0] # 0 1 2 3 순서대로 북 동 남 서 이다.
db = [0,1,0,-1]

def turn_left(): # 회전함수 구현해두기
    global d
    d -= 1
    if d == -1:
        d = 3
        
count = 1
turn_time = 0 # 4가 되면 돌아가야 돼

while True:    
    turn_left()
    na = a + da[d] # next a 로 지정해야 이동할지 말지를 결정가능하다
    nb = b + db[d]
    if visited[na][nb] == 0 and maps[na][nb] == 0:  # 방문하지 않았고 육지이면
        count += 1
        visited[na][nb] = 1 # 방문처리
        a,b = na,nb
        turn_time = 0
        continue # 이게 중요하지
    else:
        turn_time += 1
    if turn_time == 4: 
        na = a - da[d] # 뒤로가기
        nb = b - db[d]
        if maps[na][nb] == 0: # 뒤로 갈 수 있으면 뒤로가기
            a = na
            b = nb
            turn_time = 0 # 뒤로 갔으므로 turn_time 초기화
        else: # 뒤로 못가면 break
            break
        
print(count)
        
        
        
    




























