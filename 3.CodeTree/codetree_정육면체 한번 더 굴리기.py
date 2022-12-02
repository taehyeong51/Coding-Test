#   1
# 4 2 3
#   6
#   5
# 초기위치 : (0,0), 처음에는 항상 오른쪽
# 1.점수
# 주사위 움직일 때,
# 격자판 위 주사위가 놓여있는 칸에 적혀있는 숫자와 상하좌우로 인접하며
# 같은 숫자가 적혀있는 모든 칸의 합만큼 점수 얻음
#
# 2.주사위 움직임
# 주사위의 아랫면 > 보드의 해당 칸의 숫자 => 90도 시계방향으로 회전해 이동
# 주사위의 아랫면 < 보드의 해당 칸의 숫자 => 90도 반시계방향 회전
# 동일하면 그대로
# 격자판 벗어나면 방향 반사 후 뒤로 한 칸

from collections import deque
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dice = [1,2,3] # up, front, right, then bottom,back,left = 7-up,front-front,right-left


dr = [0,1,0,-1]
dc = [1,0,-1,0]
direction = 0 # 0 : 오른쪽, 1 : 아래, 2 : 왼쪽, 3 : 위
dice_pos = [0,0] # r,c
def dice_move():
    global dice,dice_pos,direction
    now_r,now_c = dice_pos[0],dice_pos[1]
    if now_r + dr[direction] < 0 or now_r + dr[direction] >= N or now_c + dc[direction] < 0 or now_c + dc[direction] >= N:
        # print("Direction reverse")
        direction_reverse()
    new_r,new_c = now_r + dr[direction],now_c + dc[direction]
    now_up,now_front,now_right = dice[0],dice[1],dice[2]
    if direction == 0:
        new_up,new_front,new_right = 7-now_right,now_front,now_up
    elif direction == 1:
        new_up, new_front, new_right = 7-now_front,now_up,now_right
    elif direction == 2:
        new_up, new_front, new_right = now_right,now_front,7-now_up
    elif direction == 3:
        new_up, new_front, new_right = now_front,7-now_up,now_right
    dice_pos = [new_r,new_c]
    dice = [new_up,new_front,new_right]

def get_score():
    global ans,direction
    now_r,now_c = dice_pos[0],dice_pos[1]
    # print("Now dice - up:{},front:{},right:{}".format(dice[0],dice[1],dice[2]))
    # print("Dice is not at ({},{}):".format(now_r,now_c))
    now_number = graph[now_r][now_c]
    q = deque()
    q.append((now_r,now_c))
    visited = [[0]*N for _ in range(N)]
    visited[now_r][now_c] = 1
    cnt = 1
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and graph[nr][nc] == now_number:
                cnt += 1
                visited[nr][nc] = 1
                q.append((nr,nc))
    now_bottom = 7 - dice[0]
    # print("Now bottom : {}, Now graph bottom : {}".format(now_bottom,now_number))
    if now_bottom > now_number:
        direction = (direction+1)%4
    elif now_bottom < now_number:
        direction = (direction-1+4)%4

    score = now_number*cnt
    # print(score)
    ans += score

def direction_reverse():
    global direction
    if direction == 0:
        direction = 2
    elif direction == 1:
        direction = 3
    elif direction == 2:
        direction = 0
    elif direction == 3:
        direction = 1


ans = 0
for _ in range(M):
    dice_move()
    get_score()
print(ans)