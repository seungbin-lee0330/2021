# 다시 풀어보기

def rotate_matrix_by_90_degree(a): # 시계방향 회전
    n = len(a) # 행
    m = len(a[0]) # 열
    result = [[0] * n for _ in range(m)] # 행이 m 열이 n으로 바뀜
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j] # 그림그려서 잘 생각해보면 된다
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length,lock_length * 2):
        for j in range(lock_length,lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key,lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0] * (3*n) for _ in range(3*n)] # 3n * 3n 크기의 새로운 자물쇠
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    for rotation in range(4):
        key = rotate_matrix_by_90_degree(key)
        for x in range(2*n):
            for y in range(2*n):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
 
























# def rotate_a_matrix_by_90_degree(a): # 암기해버리자
#     n = len(a) # 행 길이
#     m = len(a[0]) # 열 길이
#     result = [[0] * n for _ in range(m)] # 행과 열을 바꿌다
#     for i in range(n): # 원래의 행
#         for j in range(m): # 원래의 열
#             result[j][n-i-1] = a[i][j]
#     return result

# def check(new_lock):
#     lock_length = len(new_lock) // 3
#     for i in range(lock_length,lock_length * 2):
#         for j in range(lock_length,lock_length * 2):
#             if new_lock[i][j] != 1:
#                 return False
#     return True

# def solution(key, lock):
#     n = len(lock)
#     m = len(key)
#     new_lock = [[0] * (n*3) for _ in range(n*3)] # lock크기의 3배로 만들어준다!
#     for i in range(n):
#         for j in range(n):
#             new_lock[i+n][j+n] = lock[i][j] # 중심부분을 lock으로 만들어준다.
#     for rotation in range(4): # 회전을 총 4번 반복한다
#         key = rotate_a_matrix_by_90_degree(key)
#         for x in range(n*2): # 시작점이 0 n 2n 있을 수 있다
#             for y in range(n*2):
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] += key[i][j]
#                 if check(new_lock) == True:
#                     return True
#                 for i in range(m): # 자물쇠에서 열쇠를 다시 빼기
#                     for j in range(m):
#                         new_lock[x+i][y+j] -= key[i][j]
#     return False