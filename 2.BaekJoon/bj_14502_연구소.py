import sys
from itertools import combinations
import copy
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

# 풀이법
# 1. viruse에서 0인 점의 좌표를 저장한 후 combinations을 통해 모든 경우의 수 생성
# 2. 모든 경우의 수에 대해 dfs를 통해 safe area 계산

N,M = map(int,input().split())

viruses = [list(map(int,input().split())) for _ in range(N)]

def safe_area():
    return
    
candidates = []

for y in range(N):
    for x in range(M):
        if viruses[y][x] == 0:
            candidates.append((y,x))
            
candidates = list(combinations(candidates,3))

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def dfs(r,c): # infected area 검출
    global visited,viruses_,dr,dc
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and viruses_[nr][nc] == 0:
            visited[nr][nc] = 1
            viruses_[nr][nc] = 2
            dfs(nr,nc)

    
ans = 0
position = ()
asd = []
for candidate in candidates:
    viruses_ = copy.deepcopy(viruses)
    for y,x in candidate:
        viruses_[y][x] = 1

    visited = [[0]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if viruses_[r][c] == 2:
                visited[r][c] = 1
                dfs(r,c)
    res = 0            
    for _ in viruses_:
        res += _.count(0)
    if res > ans:
        ans = res
        asd = copy.deepcopy(viruses_)
        
print(ans)
