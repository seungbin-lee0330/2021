n,m = map(int,input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치 후 맵 리스트
for _ in range(n):
    data.append(list(map(int,input().split())))
dx = [0,0,-1,1] # 상하좌우
dy = [-1,1,0,0]
result = 0

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score
                
def dfs(count): # count 를 입력으로 받아야겠지!!!!
    global result # 함수안에서 변수값을 바꾸고 싶을 때 global을 사용한다
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        result = max(result,get_score())
        return
    for i in range(n):  # 이부분이 실제 구현하기 어려울거다!!!!!!
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1       
dfs(0)
print(result)