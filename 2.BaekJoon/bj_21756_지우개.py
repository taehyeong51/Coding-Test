'''
1. 홀수번 칸 모두 지우기
2. 남은 수 왼쪽으로 모으기
3. 수 하나 남으면 작업 종료 후 남은 하나의 수 출력
'''

N = int(input())
array = [i+1 for i in range(N)]

def remove_odd(input_array):
    tmp = []
    for i in range(len(input_array)):
        if i%2:
            tmp.append(input_array[i])
    return tmp

while len(array) > 1: 
    array = remove_odd(array)
    
print(array[0])