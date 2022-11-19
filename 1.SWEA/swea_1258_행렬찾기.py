import sys
sys.stdin = open("input.txt", "r")
from collections import deque
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    list_matrix = []  # (행,열,행*열)
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and graph[r][c]:
                visited[r][c] = 1
                q = deque()
                q.append((r,c))
                i_r,i_c = r,c # initial r,c
                e_r,e_c = 0,0 # end r,c
                while q:
                    now_r,now_c = q.popleft()
                    for i in range(4):
                        nr = now_r + dr[i]
                        nc = now_c + dc[i]
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and graph[nr][nc]:
                            visited[nr][nc] = 1
                            q.append((nr,nc))
                            if nr > e_r:
                                e_r = nr
                            if nc > e_c:
                                e_c = nc
                col = abs(e_c-i_c+1)
                row = abs(e_r-i_r+1)
                list_matrix.append((row,col,row*col))

    list_matrix.sort(key=lambda x:(x[-1],x[0]))
    ans = [str(matrix[0]) + " " + str(matrix[1]) for matrix in list_matrix]
    ans = " ".join(ans)
    print(f"#{tc} {len(list_matrix)} {ans}")