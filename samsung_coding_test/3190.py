n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
dir_info = [] # 방향 회전 정보
for _ in range(k):
    a,b = map(int,input().split()) # 사과의 위치
    data[a][b] = 1
l = int(input())
for _ in range(l): # 시간과 방향정보
    x,c = input().split()
    dir_info.append((int(x),c)) # x는 숫자 c는 문자 
dx = [1,0,-1,0] # 동남서북 으로 해야지
dy = [0,-1,0,1]

def turn(direction,c):
    if c == "L":
        direction = (direction - 1) % 4 # -1 을 4로 나눈 나머지는 3이다!!!!!!
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():    
    x, y = 1, 1
    data[x][y] = 2 # 뱀이 존재하는 위치를 2로 표시하는게 아이디어다
    direction = 0
    time = 0
    index = 0
    q = [(x,y)] # 뱀이 차지하고 있는 위치 정보를 저장하는게 중요하다 꼬리부터 앞쪽으로 되어있다.
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2: # 맵 안에 있고 뱀의 몸통이 아닌 위치인 경우
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx,ny))
                px,py = q.pop(0) # 사과가 없다면 꼬리를 빼버리고 맵에서도 제거한다
                data[px][py] = 0 
            elif data[nx][ny] == 1:
                data[nx][ny] =2
                q.append((nx,ny))
        else:
            time += 1
            break
        x,y = nx,ny
        time += 1
        if index < l and time == dir_info[index][0]: # index가 l보다 작다는 조건 필요한가... 없어도 될듯
            direction = turn(direction,dir_info[index][1])  
            index += 1
    return time

print(simulate())        