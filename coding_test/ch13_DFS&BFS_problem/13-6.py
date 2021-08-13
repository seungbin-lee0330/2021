from itertools import combinations
n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j)) # 선생님의 위치좌표 저장 방향별 완전탐색에 이용
        if board[i][j] == 'X':
            spaces.append((i,j)) # 빈공간은 3개를 골라내기위해 사용
            
def watch(x,y,direction): # 학생발견 : True, 학생 미발견 : False
    if direction == 0: # 상하좌우 순서대로 감시
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1        
    if direction == 1: # 하
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1           
    if direction == 2: # 좌
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1  
    if direction == 3: # 우
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    return False # 방향이 잘못 입력된경우

def process():
    for x,y in teachers: # 모든 선생님에 대해서 수행
        for i in range(4): # 모든 방향에 대해 수행
            if watch(x,y,i): # 학생을 찾아낸 경우
                return True        
    return False # 학생을 못찾은경우
    
clear = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지 여부

for data in combinations(spaces,3): # 빈 공간에서 3개를 뽑는 모든 조합을 확인
    for x,y in data:
        board[x][y] = 'O' # 장애물 설치
    if not process():
        clear = True
        break
    for x,y in data:
        board[x][y] = 'X' # 장애물 제거
if clear:
    print('YES')
    
else:
    print('NO')