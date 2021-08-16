def sequential_search(n,targe,array):
    
    for i in range(n):
        if array[i] == target:
            return i + 1
        
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")

input_data = input().split() # 값들이 리스트안에 저장된다.

n = int(input_data[0]) 
target = input_data[1]  # n,target = map(int,input().split()) 쓰면 한줄로도 가능할듯

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한칸으로 합니다")

array = input().split() # 문자열이 리스트에 저장된다.

print(sequential_search(n,target,array))


