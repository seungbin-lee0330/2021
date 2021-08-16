# 다시풀기

n = int(input())
plans = input().split() #  자동으로 리스트로 입력을 받는다
direction = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]
x,y = 1,1

for plan in plans:
    for i in range(len(direction)):
        if plan == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if 1 <= nx <= n and 1 <= ny <= n:
        x,y = nx,ny
print(x,y)





















# n = int(input())
# x,y = 1,1
# plans = input().split() # 문자열이므로 그대로 받으면 된다. 리스트로 저장된다
# move_types = ['L','R','U','D']
# dx = [0,0,-1,1] # LRUD
# dy = [-1,1,0,0]

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if 1 <= nx <= n and 1 <= ny <= n:
#         x,y = nx,ny
                
# print(x,y)
























