'''
NxN 격자판
돌 - 가로,세로,대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분 있는지 없는지 체크

Sol.
가로,세로,대각선으로 각각 dfs 실행
'''
import sys
sys.stdin = open("input.txt", "r")

from collections import deque
T = int(input())

dr = [1,0,-1,0,-1,-1,1,1]
dc = [0,1,0,-1,-1,1,1,-1]

def dfs(r,c,d,cnt): # d : direction, -1이면 정해지지 않음, 0 - 왼쪽 위, 1 - 오른쪽 위, 2 - 오른쪽 아래, 3 - 왼쪽 아래
    global omok
    if omok:
        return
    if cnt == 5:
        omok = True
        return
    if d == -1:
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and graph[nr][nc]=='o':
                visited[nr][nc] = 1
                dfs(nr,nc,i,cnt+1)
                visited[nr][nc] = 0
    else:
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and graph[nr][nc]=='o':
            visited[nr][nc] = 1
            dfs(nr,nc,d,cnt+1)
            visited[nr][nc] = 0
    
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(input()) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    omok = False
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and graph[r][c] == 'o':
                visited[r][c] = 1
                dfs(r,c,-1,1)
                if omok:
                    break
        if omok:
            break
                
    if omok:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")


            
            
            