from bisect import bisect_left,bisect_right # bisect는 숫자가 들어가 자리를 반환!
# 여러개 있을경우 각각 가장 왼쪽과 오른쪽을 반환하고 아니면 같은 인덱스를 반환한다

n,x = map(int,input().split()) # 이미 정렬되어 있다고 문제에서 주어졌다.
data = list(map(int,input().split()))

left = bisect_left(data,x) 
right = bisect_right(data,x)
count = right - left

if count == 0:
    print(-1)
else:
    print(count)