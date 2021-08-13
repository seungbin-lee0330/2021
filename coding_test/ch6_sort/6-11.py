# 다시 풀어보기



n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1]))) # 튜플 형태로 저장
    
array = sorted(array,key=lambda student: student[1]) # 키를 이용해 점수를 기준으로 정렬
for student in array:
    print(student[0],end=' ')    
    











