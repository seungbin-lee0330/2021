n = int(input())
data = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())
min_value = 1e9 # 최솟값 최댓값 초기화
max_value = -1e9

def dfs(i,now): # i는 사용한 숫자개수 now는 현재 값
    global min_value, max_value, add, sub, mul, div # 함수안에서도 값을 수정해주기 위해 전역변수 global로 선언
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0: # 연산이 어떤 순서로 수행될지 몰라서 되돌리는작업이 포함된다
            add -= 1 # 수행
            dfs(i+1,now + data[i]) # dfs
            add += 1 # 되돌리기
        if sub > 0:
            sub -= 1
            dfs(i+1,now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1,now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1,now / data[i])
            div += 1
dfs(1,data[0])
print(max_value)
print(min_value)