'''
N*N 보드에 N개의 퀸을 서로 공격하지 못하도록 놓는 경우의 수
'''
import sys
sys.stdin = open("input.txt", "r")


T = int(input())

def adjacent(x):
    for row in range(x):
        if graph[x] == graph[row] or abs(graph[x]-graph[row]) == x-row:
            return False
    return True

def dfs(L):
    global ans
    if L == N:
        ans += 1
    else:
        for i in range(N):
            graph[L] = i # 체스판 L행 i열에 퀸을 둠
            if adjacent(L):
                dfs(L+1)
            graph[L] = 0

for tc in range(1,T+1):
    N = int(input())
    graph = [0 for _ in range(N)]
    ans = 0
    dfs(0)
    print(f"#{tc} {ans}")
