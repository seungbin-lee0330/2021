n = int(input())
k = int(input())

data = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
dir_info = [] # 방향 회전 정보

for _ in range(k):
    a,b = map(int,input().split())
    data[a][b] = 1
    
l = int(input())

for _ in range(l):
    x,c = input().split()
    dir_info.append((int(x),c)) # x는 숫자 c는 문자 
    
dx = [0,1,0,-1] # 동 남 서 북
dy = [1,0,-1,0]

def turn(direction,c):
    
    if c == "L":
        direction = (direction - 1) % 4
    
    else:
        direction = (direction + 1) % 4
        
    return direction

def simulate():
    
    x, y = 1, 1
    data[x][y] = 2 # 뱀이 존재하는 위치를 2로 표시
    direction = 0
    time = 0
    index = 0
    q = [(x,y)] # 뱀이 차지하고 있는 위치 정보 꼬리부터 앞쪽으로 되어있다.
    while True:
        
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2: # 맵 안에 있고 뱀의 몸통이 아닌 위치인 경우
            
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx,ny))
                px,py = q.pop(0)
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