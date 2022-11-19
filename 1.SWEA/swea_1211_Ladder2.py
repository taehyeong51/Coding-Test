from collections import deque
import sys
sys.stdin = open("input.txt", "r")

dr = [0,0,-1]
dc = [1,-1,0]

def ladder(r,c):

    q = deque()
    q.append((r,c))
    visited = [[0] * 100 for _ in range(100)]
    visited[r][c] = 1
    cnt = 0
    while q:
        r,c = q.popleft()
        go = False
        if r == 0:
            return cnt,c
        for i in range(3):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 100 and 0 <= nc < 100 and graph[nr][nc] == 1 and not visited[nr][nc] and not go:
                cnt += 1
                go = True
                visited[nr][nc] = 1
                q.append((nr,nc))

for tc in range(1,11):
    input()
    graph = [list(map(int,input().split())) for _ in range(100)]
    ans = 999999999999
    ans_c = -1
    for c in range(100):
        if graph[99][c] == 1:
            tmp,tmp_c = ladder(99,c)
            if tmp < ans:
                ans = tmp
                ans_c = tmp_c


    print(f"#{tc} {ans_c}")