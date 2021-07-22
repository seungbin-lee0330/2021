# 어려움 다시 풀어보기

f = open("13-2.txt")
input = f.readline

n,m = map(int,input().split())

data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int,input().split())))

dx = [0,0,-1,1] # 상하좌우
dy = [-1,1,0,0]

result = 0

def virus(x,y):
    for i in range(4): # 4방향 모두 확인
        
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                
                temp[nx][ny] = 2
                virus(nx,ny) # 재귀적으로 모두 확인
                
def get_score():
    
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
                
    return score

def dfs(count):
    global result
    
    if count == 3: # 울타리가 3개 설치된 경우
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
                
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
                    
        result = max(result,get_score())
        return
    
    for i in range(n):
        for j in range(m):
            
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count) # 재귀적으로 실행!!!
                data[i][j] = 0
                count -= 1 
                
dfs(0)
print(result)