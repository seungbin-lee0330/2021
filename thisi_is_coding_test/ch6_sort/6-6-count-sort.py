# 계수정렬의 시간 복잡도는 n + k 로 데이터의 범위가 한정적일 때 유용하다. n은 데이터의 개수 k는 최댓값

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2] # 모든 원소가 0 이상이라고 가정한다
count = [0] * (max(array) + 1) # 횟수를 모두 0으로 초기화

for i in range(len(array)):
    count[array[i]] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end= ' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력