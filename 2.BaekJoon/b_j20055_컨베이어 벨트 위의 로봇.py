# 컨베이어 벨트를 감싼 벨트의 길이 : 2N
# i번칸 내구도 - A_i
# 1번칸 : 올리는 위치-로봇 올릴 수 있음, N번칸 : 내리는 위치
# 로봇을 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 1만큼 감소

# 로봇 옮기기
# 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
# 2. 가장 먼저 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
# 만약 이동할 수 없으면 가만히 있음
# 2-1. 로봇 이동하기 위해서는 이동하려는 칸에 로봇 X, 내구도 1 이상
# 3. 올리는 위치에 있는 칸의 내구도 0 아니면 올리는 위치에 로봇 올림
# 4. 내구도가 0인 칸의 개수가 K개 이상이면 과정 종료, 그렇지 않으면 1번으로 돌아감
# 종료되었을 때, 몇 번째 단계가 진행 중이었는지 구해보자.

import sys
from collections import deque

input = sys.stdin.readline

N,K = map(int,input().split())
indurances = deque(list(map(int,input().split())))
robots = deque(0 for _ in range(N))
cnt = 0
while True:
    cnt += 1
    indurances.rotate(1)
    robots.rotate(1)
    robots[-1] = 0 # 로봇 하차

    if sum(robots):
        for idx in range(N-2,-1,-1):
            now = idx
            next = now + 1 
            now_robot = robots[now]
            next_robot = robots[next]
            next_indurances = indurances[next]
            if now_robot != 0 and next_robot == 0 and next_indurances >= 1:
                robots[next] = now_robot
                robots[now] = 0
                indurances[next] -= 1
        robots[-1] = 0
    
    if robots[0] == 0 and indurances[0] >= 1:
        robots[0] = cnt # 로봇 상차
        indurances[0] -= 1
    # 4. 내구도가 0인 칸의 개수가 K개 이상이면 과정 종료, 그렇지 않으면 1번으로 돌아감

    stop_cnt = indurances.count(0)
    if stop_cnt >= K:
        print(cnt)
        break

        


