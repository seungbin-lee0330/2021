array = [('바나나',2),('사과',5),('당근',3)]
def setting(data):
    return data[1]
result = sorted(array, key = setting) # sorted 함수의 key 값으로는 하나의 함수가 들어가야 한다
# result = sorted(array, key = lambda x: x[1], reverse = True) #lambda x 는 함수 이름
print(result)