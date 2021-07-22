from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        
        if board[i][j] == 'T':
            teachers.append((i,j))
            
        if board[i][j] == 'X':
            spaces.append((i,j))
            
def watch(x,y,direction): # 학생발견 : True, 학생 미발견 : False
    
    if direction == 0: # 상하좌우 순서대로 감시
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1        

    if direction == 1: # 
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1    
            
    if direction == 2: # 
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1  
            
    if direction == 3:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
            
    return False

def process():
    
    for x,y, in teachers: # 모든 선생님에 대해서 수행
        
        for i in range(4):
            if watch(x,y,i):
                return True
            
    return False
    
find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지 여부

for data in combinations(spaces,3): # 빈 공간에서 3개를 뽑는 모든 조합을 확인
    
    for x,y in data:
        board[x][y] = 'O'
        
    if not process():
        find = True
        break
    
    for x,y in data:
        board[x][y] = 'X'

if find:
    print('YES')
    
else:
    print('NO')