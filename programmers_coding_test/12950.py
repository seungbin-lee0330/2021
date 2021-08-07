def solution(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer # zip 함수의 이중 사용 알아두기

def sumMatrix(A,B):
    
    C = [[0] * len(A[0]) for i in range(len(A))] # 행과 열의 크기를 알 때 2차원 배열 초기화 방법
    for i in range(len(A)) : # 2차원 배열의 덧셈을 하는 방법
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j] 
    return C