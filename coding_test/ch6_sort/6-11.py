n = int(input())

array = []

for i in range(n):
    input_data = input().split()
    
    array.append((input_data[0],int(input_data[1]))) # 점수는 정수형으로 변환하여 저장
    
array = sorted(array, key=lambda student: student[1]) # 키를 이용하여 점수를 기준으로 정렬하기

for student in array:
    print(student[0], end= ' ')