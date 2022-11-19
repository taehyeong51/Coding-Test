'''
A1,A2,...,A_N의 N개 자연수
최소 1개 이상 수 선택하여 그 합이 K가 되는 경우의 수
'''
import sys
# sys.stdin = open("input.txt", "r")
from itertools import combinations as cb
T = int(input())


def solve(idx, sum):
    global cnt
    if idx >= N:
        return
    temp = sum + A[idx]
    if temp == K:
        cnt += 1

    solve(idx + 1, sum)
    solve(idx + 1, temp)

for tc in range(1,T+1):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    cb_list = []
    for i in range(1,len(A)+1):
        cb_list += list(cb(A,i))
    cb_list = list(map(sum,cb_list))

    cnt = 0
    solve(0,0)
    print(f"#{tc} {cb_list.count(K)}")
    print(cnt)
