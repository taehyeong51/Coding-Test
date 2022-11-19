'''
9자리 이하 음이 아닌 정수 N
한 쌍의 숫자를 골라 바꾸거나 바꾸지 않음으로써 새로운 수 M을 만듦(단 맨 앞자리 != 0)
M의 최솟값과 최댓값
'''
import sys
# sys.stdin = open("input.txt", "r")

def l2i(numbers):
    return int("".join(list(map(str,numbers))))

def get_all(numbers):
    global list_numbers
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            numbers[i],numbers[j] = numbers[j],numbers[i]
            if l2i(numbers) not in list_numbers and numbers[0] != 0:
                list_numbers.append(l2i(numbers))
            numbers[i], numbers[j] = numbers[j], numbers[i]

T = int(input())
for tc in range(1,T+1):
    numbers = list(map(int,list(input())))
    list_numbers = [l2i(numbers)]
    get_all(numbers)

    print(f"#{tc} {min(list_numbers)} {max(list_numbers)}")
