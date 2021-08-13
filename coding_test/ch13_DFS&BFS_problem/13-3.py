from collections import deque

n,k = map(int,input().split()) # n*n 크기 시험관, k가지의 바이러스 종류
graph = [] # 전체 시험관 정보
data = [] # 바이러스 정보

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j)) # 위치,경과시간,x좌표,y좌표
data.sort() # 가장 낮은 번호부터 증식한다!!
q=deque(data)

s,x,y = map(int,input().split()) # time,x좌표,y좌표
dx = [0,0,-1,1] # 상하좌우
dy = [-1,1,0,0]

while q:
    virus,s_,x_,y_ = q.popleft()
    if s_ == s: # s초가 지난 경우 빠져나옴
        break
    for i in range(4):
        nx_ = x_ + dx[i]
        ny_ = y_ + dy[i]
        if 0 <= nx_ < n and 0 <= ny_ < n:
            if graph[nx_][ny_] == 0:
                graph[nx_][ny_] = virus
                q.append((virus,s_ + 1,nx_,ny_)) # 시간늘어남 위치바뀜
                
print(graph[x - 1][y - 1])
    
    