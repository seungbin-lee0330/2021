# n,k = map(int,input().split())

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# a.sort()
# b.sort()         # b는 내림차순으로 정렬하는 것이 인덱스 차원에서 편했을 것이다.

# for i in range(k):
#                                       # 최대값을 만들어야 하므로 a보다 b가 클때만 바꿔야지 아니면 break로 빠져나가야 한다
#     a[i],b[n-1-i] = b[n-1-i],a[i]
    
# print(sum(a))





# n,k = map(int,input().split())

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# a.sort()
# b.sort(reverse=True)

# for i in range(k):
#     if a[i] < b[i]:
#         a[i], b[i] = b[i], a[i]
        
#     else:
#         break
    
# print(sum(a))