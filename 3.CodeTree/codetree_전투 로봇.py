# 1. 물고기 M, [아기 상어 1마리 - 크기 2], 1초에 상하좌우로 인접한 한 칸씩 이동
# 이때 자기보다 큰 물고기 있는 칸 지나갈 수 없음
# 자기보다 작은 물고기만 먹을 수 없음
# 자기랑 같은 크기의 물고기 먹을 수 X, 지나갈 수 O
#
# 어디로 이동할 지 결정하는 방법
# 1. 더 이상 먹을 수 있는 물고기 공간에 없으면 엄마 상어에게 도움 요청 -> 끝
# 2. 먹을 수 있는 물고기 1마리 -> 그 물고기 먹으러 감
# 3. 먹을 수 있는 물고기 >= 1 -> 가까운 물고기 먹으러 감
# 3-1. 거리 : 지나야하는 칸의 개수의 최솟값
# 3-2. 거리가 가까운 물고기 > 1 : 행,열 순으로
#
# 이동에 1초 걸림, 해당 칸으로 이동하자마자 물고기 먹음, 먹으면 빈 칸 됨
# 자신의 크기와 같은 수의 물고기를 먹을 때 크기 1 증가

# 엄마 상어에게 도움 요청하는 시간 출력
from collections import deque
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

#initialize
ans = 0
size_babyshark = 2
b_r,b_c = 0,0
distances = []
dr = [1,0,-1,0]
dc = [0,1,0,-1]
candidates = []
#def functions
def in_range(rr,cc):
    if 0<=rr<N and 0 <=cc<N:
        return True
    else:
        return False

def call_mom1():
    is_call = True
    for r in range(N):
        for c in range(N):
            if graph[r][c] != 9 and graph[r][c] != 0 and graph[r][c] < size_babyshark:
               return False
    if is_call:
        return True

def call_mom2():
    is_call = True
    for r in range(N):
        for c in range(N):
            if graph[r][c] != 9 and graph[r][c] != 0:
                return False
    if is_call:
        return True

def get_babyshark_pos():
    global b_r,b_c
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 9:
                b_r,b_c = r,c
                return

# 여기서 도달할 때 경로 세면 가지치기 가능할거같음
def is_able_to_get_fish(fish_r,fish_c,shark_r,shark_c): # bfs 통해서 해당 물고기로 갈 수 있는지 조사
    global res
    path = 0
    q = deque()
    q.append((shark_r,shark_c,path))
    visited_bfs = [[0] * N for _ in range(N)]
    visited_bfs[shark_r][shark_c] = 1
    while q:
        r,c,path = q.popleft()
        if r == fish_r and c == fish_c:
            res = path
            return True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if in_range(nr,nc) and graph[nr][nc] <= size_babyshark and visited_bfs[nr][nc] == 0:
                visited_bfs[nr][nc] = 1
                q.append((nr,nc,path+1))
    return False


def get_candidates():
    global candidates
    candidates = []
    for r in range(N):
        for c in range(N):
            if graph[r][c] != 9 and 0 < graph[r][c] < size_babyshark:
                candidates.append((r,c))
    candidates.sort(key=lambda x:(x[0],x[1]))

def eat_fish(fish_r,fish_c,shark_r,shark_c):
    global size_babyshark,b_r,b_c,eat_cnt
    eat_cnt += 1
    graph[shark_r][shark_c] = 0
    # print("상어({},{}),크기:{}가 물고기({},{}),크기:{} 잡아먹음".format(shark_r,shark_c,size_babyshark,fish_r,fish_c,graph[fish_r][fish_c]))
    # print("eat cnt:",eat_cnt)
    if eat_cnt == size_babyshark:
        # print("현재 상어{}가 {} 잡아먹어서 벌크업".format(size_babyshark,graph[fish_r][fish_c]))
        # print("{}->{}".format(size_babyshark,size_babyshark+1))
        size_babyshark += 1
        eat_cnt = 0
    graph[fish_r][fish_c] = 9
    b_r,b_c = fish_r,fish_c

def show_graph():
    print("")
    for _ in graph:
        print(_)
get_babyshark_pos()  # baby shark pos 업데이트


eat_cnt = 0
while True:
    # show_graph()
    if call_mom1() or call_mom2():
        break
    # main
    get_candidates()  # candidates 리스트에 먹을 수 있는 물고리 리스트들 저장
    # print("candidates:",candidates)
    edible_fish = []
    # idx = 0
    res = 9999999
    for fish_r, fish_c in candidates:  # graph에 있는 물고기들에 대해
        # for is_able_to_get_fish
        if is_able_to_get_fish(fish_r, fish_c, b_r, b_c):  # 만약 상어가 먹으러 갈 수 있다면
            # visited = [[0] * N for _ in range(N)]
            # is_changed = False
            # get_min_distance(fish_r, fish_c, b_r, b_c, 0)
            # if is_changed:
            edible_fish.append((res, fish_r, fish_c))  # 리스트에 (최단거리,r,c) 저장

        # idx += 1
    if edible_fish:
        edible_fish.sort(key=lambda x: (x[0], x[1], x[2]))
        min_time, target_r, target_c = edible_fish[0]
        eat_fish(target_r, target_c, b_r, b_c)
        #
        # print("")
        # print(edible_fish)
        # print(distances_list)
        ans += min_time
        # print("추가 시간:{},현재 총 시간:{}".format(min_time,ans))
    else:
        break

print(ans)

