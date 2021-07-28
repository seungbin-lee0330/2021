# 어려운 문제 다시풀기
















# n,m = map(int,input().split())

# a,b,d = map(int,input().split())

# maps = []

# visited =[[0] * m for _ in range(n)] # 방문한 위치를 저장하기 위함

# visited[a][b] = 1 

# for i in range(n):
    
#     maps.append(list(map(int,input().split())))

# da = [0,1,0,-1] # 북동남서 d와 인덱스 맞춰주기 위해
# db = [-1,0,1,0]


# def turn_left(): # 회전함수 구현해두기
#     global d
#     d -= 1
#     if d == -1:
#         d = 3
        
# count = 1
# turn_time = 0 # 4가 되면 돌아가야 돼

# while True:
    
#     turn_left()
#     na = a + da[d] # next a
#     nb = b + db[d]
    
#     if visited[na][nb] == 0 and maps[na][nb] == 0:  # 방문하지 않은 육지이면
        
#         count += 1
#         visited[na][nb] = 1
#         a,b = na,nb
#         turn_time =0
#         continue # 이게 중요하지
    
#     else:
#         turn_time += 1
        
#     if turn_time == 4:
        
#         na = a - da[d]
#         nb = b - db[d]
        
#         if maps[na][nb] == 0: # 뒤로 갈 수 있으면 뒤로가기
            
#             a,b = na,nb
#             turn_time = 0 # 뒤로 갔으므로 turn_time 초기화
            
#         else:
#             break
        
# print(count)
        
        
        
    




























