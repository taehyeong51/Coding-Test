from collections import defaultdict
import time

# 1. 미세먼지 확산
# (r,c) 인접한 네 방향
# 인접한 칸에 공기청정기 or 칸이 없으면 확산 X
# 확산되는 양 : A(r,c) / 5, 소수점 버림
# (r,c)에 남은 미세먼지 양 : A(r,c) - (A(r,c)/5)*확산된 방향 개수

# 2. 공기청정기 작동
# 위쪽 공기청정기 : 반시계방향 순환
# 아래쪽 공기청정기 : 시계방향 순환

# T초 지난 후 방에 남아있는 미세먼지의 양

R,C,T = map(int,input().split()) # R - row, C - column, T - T초

graph = [list(map(int,input().split())) for _ in range(R)]

air_pos = []
# 공기 청정기 위치
for r in range(R):
    c = 0
    if graph[r][c] == -1:
        air_pos.append((r,c)) 
        air_pos.append((r+1,c))
        break
    
def not_dust(nr,nc):
    if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != -1: # 공기청정기가 아닐때만, 즉 먼지가 없어도 True
        return True
    return False

def air_upper():
    r,c = air_pos[0]
    status = 0
    dr = [0,-1,0,1]
    dc = [1,0,-1,0]
    before = 0
    r += dr[status]
    c += dc[status]
    while True:
        if c+dc[status] >= C or r+dr[status] < 0 or c+dc[status] < 0:
            status += 1
        nr = r + dr[status]
        nc = c + dc[status]
        if graph[r][c] == -1:
            break
        graph[r][c],before = before,graph[r][c]
        r = nr
        c = nc
def air_lower():
    r,c = air_pos[1]
    status = 0
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    before = 0
    r += dr[status]
    c += dc[status]
    while True:
        if c+dc[status] >= C or r+dr[status] >= R or c+dc[status] < 0:
            status += 1
        nr = r + dr[status]
        nc = c + dc[status]
        if graph[r][c] == -1:
            break
        graph[r][c],before = before,graph[r][c]
            
        r = nr
        c = nc

def step_one():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_arr = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0 and graph[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        tmp_arr[nx][ny] += graph[i][j] // 5
                        tmp += graph[i][j] // 5
                graph[i][j] -= tmp

    for i in range(R):
        for j in range(C):
         graph[i][j] += tmp_arr[i][j]
                
def step_two():
    air_upper()
    air_lower()

def count_dust():
    global ans
    for r in range(R):
        for c in range(C):
            if not_dust(r,c):
                ans += graph[r][c]
    print(ans)
ans = 0

def print_dust():
    for _ in graph:
        print(_)
        
for _ in range(T):
    # print("1.확산 전")
    # print_dust()
    step_one()
    # print("2.확산 후")
    # print_dust()
    step_two()
    # print("3.공기청정기 후")
    # print_dust()
    
count_dust()