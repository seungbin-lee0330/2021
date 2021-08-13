array = [7,5,9,0,3,1,6,2,4,8] # 삽입정렬의 시간복잡도 여전히 n^2

for i in range(1,len(array)): # i는 1부터 마지막까지 확인한다
    for j in range(i,0,-1): # 인덱스  i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j] # 스왑
        else:     ### 자기보다 작은 데이터를 만나면 그 위치에서 멈춰야한다 - 효율성 측면에서 생각!!!
            break
        
print(array)

