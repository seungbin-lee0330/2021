n,k = map(int,input().split())

result = 0

while True:
    
    target = (n//k) *k # n과 가장 가까운 k의 배수
    result += (n-target)
    n = target
    
    if n < k:
        break

    result += 1
    n //= k

result += (n-1) # 1이 될때까지 빼주어야 하므로
print(result)