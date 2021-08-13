# 어려운 문제 다시풀기








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
        visited[na][nb] = 1
        a, = na
        b = nb
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
        else:
            break
        
print(count)
        
        
        
    




























