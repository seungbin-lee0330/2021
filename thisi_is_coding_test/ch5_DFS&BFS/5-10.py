n,m = map(int,input().split())  # 0을 1로 만들어버리는 테크닉으로 푼다!!!!!!!
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    
def dfs(x,y): # dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False # 주어진 범위를 벗어나는 경우 바로 종료
    if graph[x][y] == 0: 
        graph[x][y] = 1 # 방문처리
        dfs(x-1,y) # 상하좌우 재귀적!!!으로 모두 체크해서 모두 1로 만들어 버린다!!!
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)



