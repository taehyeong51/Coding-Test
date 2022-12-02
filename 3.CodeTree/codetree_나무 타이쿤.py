# 1. n x n 격자에 서로 다른 높이의 리브로수 주어짐
# 특수 영양제 : 1x1 땅에 있는 리브로수의 높이 1 증가, 만약 씨앗만 있는 경우 높이 1의 리브로수 생성
# 초기 특수 영양제 : n x n 격자 최하단에 4개
# 이동규칙 = (이동 방향, 이동 칸 수), 단 격자 밖으로 나가면 반대편으로 돌아옴
#
# 규칙
# 1. 특수 영양제 이동
# 2. 이동 시킨 후 해당 땅에 특수 영양제 투입
# 3. "특수 영양제 투입한 리브로수" 는 "대각선으로 인접한 방향에 높이가 1 이상인 리브로수의 수" 만큼 높이 더 성장,
#                                                                                 단 격자 벗어나면 X
# 4. 특수 영양제 투입한 리브로수 제외하고 높이 2 이상인 리브로수는 높이 2를 베어서 잘라낸 리브로수로 특수 영양제 사고
#     해당 위치에 특수 영양제 올려둠

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dr = [0,-1,-1,-1,0,1,1,1]
dc = [1,1,0,-1,-1,-1,0,1]

dgs_r = [1,1,-1,-1]
dgs_c = [1,-1,1,-1]
drugs = [[0]*N for _ in range(N)]
drugged_area = []
# 초기 특수 영양제 : n x n 격자 최하단에 4개
for r in range(N-2,N):
    for c in range(2):
        drugs[r][c] = 1
def move_drugs():
    global drugs,drugged_area
    tmp = [[0]*N for _ in range(N)]
    drugged_area = []
    for r in range(N):
        for c in range(N):
            if drugs[r][c] != 0:
                nr = (r + dr[direction-1]*P)%N
                nc = (c + dc[direction-1]*P)%N
                tmp[nr][nc] = 1
                drugged_area.append((nr,nc))
    drugs = tmp

def grow():
    global graph,drugs
    for r,c in drugged_area:
        graph[r][c] += 1
    for r,c in drugged_area:
        for i in range(4):
            nr = r + dgs_r[i]
            nc = c + dgs_c[i]
            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] >= 1:
                graph[r][c] += 1
    tmp_drugs = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if graph[r][c] >= 2 and drugs[r][c] == 0:
                graph[r][c] -= 2
                tmp_drugs[r][c] = 1
    drugs = tmp_drugs

for _ in range(M):
    direction, P = map(int, input().split())  # (방향:1~8,이동칸 수)
    move_drugs()
    grow()



ans = 0
for r in range(N):
    for c in range(N):
        ans += graph[r][c]
print(ans)