from collections import deque
N,M = map(int,input().split())


graph = [list(map(int,list(input()))) for _ in range(N)]

q = deque()
q.append((0,0,1))
dr = [1,0,-1,0]
dc = [0,1,0,-1]

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
while q:
    r,c,dist = q.popleft()
    if r == N-1 and c == M-1:
        print(dist)
        break
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and graph[nr][nc] == 1:
            visited[nr][nc] = 1
            q.append((nr,nc,dist+1))
