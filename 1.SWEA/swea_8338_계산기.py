'''
a1,a2,...,a_N : 총 N개의 수
+ or -
왼쪽에서 오른쪽으로 차례대로 계산
최대값

Sol.
dfs
'''
import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

def dfs(L,number):
    # print("L:",L)
    # print("number:",number)
    global tmp
    if number > tmp:
        tmp = number
    if number < tmp:
        return
    if L == N-1:
        return
    dfs(L+1,number+numbers[L+1])
    dfs(L+1,number*numbers[L+1])

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    tmp = 0
    dfs(0,numbers[0])
    print(f"#{tc} {tmp}")
