n = int(input())

x,y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        
        if plan == move_types[i]:
            next_x = x + dx[i]
            next_y = y + dy[i]
            
    if next_x < 1 or next_y < 1 or next_x > n or next_y > n:
        continue
    
    x, y = next_x, next_y
    
print(x,y)    