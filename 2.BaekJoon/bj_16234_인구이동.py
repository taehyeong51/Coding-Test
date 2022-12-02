import sys
from collections import deque
import time
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N,L,R = map(int,input().split())

people = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
dr = [1,-1,0,0]
dc = [0,0,1,-1]

while True:
    visited = [[0]*N for _ in range(N)]
    gonogo = True
    
    
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                pos= [(r,c)]
                visited[r][c] = 1
                q = deque()
                q.append((r,c))
                sum_people = people[r][c]
                num_people = 1
                while q:
                    r,c = q.popleft()
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                            if L <= abs(people[r][c] - people[nr][nc]) <= R:
                                visited[nr][nc] = 1
                                pos.append((nr,nc))
                                q.append((nr,nc))
                                sum_people += people[nr][nc]
                                num_people += 1
                change_people = sum_people // num_people
                if num_people >= 2:
                    gonogo = False
                    for r,c in pos:
                        people[r][c] = change_people
    if gonogo:
        
        break
    cnt += 1
              
print(cnt)