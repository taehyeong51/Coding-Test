"""
1. 모레 토네이도 이동
2. 주어진 비율대로 모래 흩날리기, 이때 주어진 비율을 4 방향으로 수정해줘야 함
    모래는 격자 밖으로 이동 가능
3. (0,0)에 도착하면 소멸, 격자 밖으로 나간 모래의 양
"""
from math import floor
import copy
N = int(input()) # N : 3~499
graph = [list(map(int,input().split())) for _ in range(N)]
s_r,s_c = N//2, N//2 # 출발점

# idx = 0 : 왼쪽
ratio = [[0]*5 for _ in range(5)]
ratio[0][2] = 0.02
ratio[1][1],ratio[1][2],ratio[1][3] = 0.10,0.07,0.01
ratio[2][0] = 0.05
ratio[3][1],ratio[3][2],ratio[3][3] = 0.1,0.07,0.01
ratio[4][2] = 0.02
pos_alpha = [(0,-1),(1,0),(0,1),(-1,0)]
def show():
    for _ in graph:
        print(_)
def rotate_90(a):
    return list(map(list, list(zip(*a[::]))))[::-1]
def scatter(r,c,idx):
    global ans

    ratio_copy = copy.deepcopy(ratio)
    for _ in range(idx):
        ratio_copy = rotate_90(ratio_copy)
    sand = graph[r][c]
    a_r,a_c = r + pos_alpha[idx][0], c + pos_alpha[idx][1]
    alpha_sand = 0
    for rr in range(5):
        for cc in range(5):
            if ratio_copy[rr][cc]:
                nr = r + rr - 2
                nc = c + cc - 2
                scattered_sand = floor(sand*ratio_copy[rr][cc])
                alpha_sand += scattered_sand
                if 0 <= nr < N and 0 <= nc < N:
                    graph[nr][nc] += scattered_sand
                else:
                    ans += scattered_sand
    if 0 <= a_r < N and 0 <= a_c < N:
        graph[a_r][a_c] += sand - alpha_sand
    else:
        ans += sand - alpha_sand
    graph[r][c] = 0

def move_tornado():
    # 토네이도의 이동 칸 수
    # N = 3 일때
    # 1,1,2,2,2
    # N = 5 일때
    # 1,1,2,2,3,3,4,4,4
    # N = 7 일때
    # 1,1,2,2,3,3,4,4,5,5,6,6,6
    # N = 9일때
    # 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6,7,7,8,8,8
    # 마지막 N-9만 3번 반복, 그전까지는 반시계방향으로 두 번씩
    tornado_number = []
    for i in range(1,N):
        if i != N-1:
            for _ in range(2):
                tornado_number.append(i)
        else:
            for _ in range(3):
                tornado_number.append(i)
    dr = [0,1,0,-1]
    dc = [-1,0,1,0]
    r = s_r
    c = s_c
    for idx,n in enumerate(tornado_number):
        for _ in range(n):
            idx %= 4
            r += dr[idx]
            c += dc[idx]
            scatter(r,c,idx)

ans = 0
move_tornado()

print(ans)


