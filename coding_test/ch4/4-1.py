# 다시풀기














# n = int(input())

# x,y = 1,1

# plans = input().split() # 문자열이므로 그대로 받으면 된다. 리스트로 저장된다

# move_types = ['L','R','U','D']

# dx = [0,0,-1,1]
# dy = [-1,1,0,0]

# for plan in plans:
#     for i in range(len(move_types)):
        
#         if plan == move_types[i]:
            
#             if 1 <= x + dx[i] <= n:
#                 x += dx[i]
            
#             if 1 <= y + dy[i] <= n:
#                 y += dy[i]
                
# print(x,y)


























n = int(input())

x,y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):

        if plan == move_types[i]:
            
            n_x = x + dx[i] # next x의 좌표
            n_y = y + dy[i]
            
    if 1 <= n_x <= n and 1<= n_y <= n:
            
        x,y = n_x,n_y # 한번에 해주는게 용이하지
        
print(x,y)    
