'''
우승 시 보너스 상금 획득
주어진 숫자판들 중 두 개 선택해 정해진 횟수만큼 자리 교환 가능
오른쪽 끝에서부터 1원, 왼쪽으로 갈 수록 *10
- 주어진 횟수만큼만 교환이 반드시 이루어짐
- 동일한 위치의 교환 중복 가능

정해진 횟수만큼 숫자판 교환했을 때 받을 수 있는 가장 큰 금액

1. 가장 큰 수 만드는 dfs 횟수 L 구하기
2. 만약 L < 교환횟수이면 가장 큰 수를 다시 (교환횟수-L)번만큼 섞어서 그 다음으로 큰 수 만들기
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
def merge(list_numbers):
    return int("".join(list_numbers))
def dfs(L,cnt):
    global used,tmp_numbers
    if L == cnt:
        tmp = merge(numbers)
        if tmp > tmp_numbers:
            tmp_numbers = tmp
        return
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            numbers[i],numbers[j] = numbers[j],numbers[i]
            if merge(numbers) not in used[L]:
                used[L].append(merge(numbers))
                dfs(L+1,cnt)
            numbers[j],numbers[i] = numbers[i],numbers[j]


for test_case in range(1,T+1):
    numbers,cnt = input().split()

    numbers = list(numbers)

    tmp_numbers = 0
    max_numbers = int("".join(sorted(numbers,reverse=True)))
    cnt = int(cnt)
    used = [[] for _ in range(11)]
    dfs(0,cnt)
    print(f"#{test_case} {tmp_numbers}")
