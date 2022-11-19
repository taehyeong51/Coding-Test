'''
NxN 격자판
'.' : 비어있음
'#' : 막혀있음
이때 막혀있는 칸들이 하나의 정사각형 이루는지 판단

Sol. 
1. bfs로 하나의 사각형 완성 후 (시작 r,c, 끝 r,c),블럭 갯수 구함
2-1. 만약 블럭 갯수 == 1 이면 yes
2-2. 블럭 갯수 != 1 이면 끝r-시작r == 끝c-시작c 이고 (끝r-시작r) ** 2 == 블럭 갯수이면 yes else no
'''
from collections import deque
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dr = [0,1]
dc = [1,0]
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(input()) for _ in range(N)]
    is_blocked = False
    is_possible = True
    rc = []
    for r in range(N):
        for c in range(N):
            if is_blocked and not visited[r][c] and graph[r][c] == '#':
                is_possible = False
                break
            if not is_blocked and graph[r][c] == '#':
                is_blocked = True
                q = deque()
                q.append((r,c))
                visited = [[0]*N for _ in range(N)]
                visited[r][c] = 1
                rc = [r,c,0,0]
                block_cnt = 1
                while q:

                    r,c = q.popleft()
                    for i in range(2):

                        nr = r + dr[i]
                        nc = c + dc[i]

                        if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == '#' and not visited[nr][nc]:
                            visited[nr][nc] = 1
                            if nr > rc[2]:
                                rc[2] = nr
                            if nc > rc[3]:
                                rc[3] = nc
                            q.append((nr,nc))
                            block_cnt += 1
    if block_cnt == 1:
        print(f"#{test_case} yes")
        continue
    if is_possible and rc and rc[2]-rc[0] == rc[3]-rc[1] and (abs(rc[2]-rc[0]+1))**2 == block_cnt:
        print(f"#{test_case} yes")
    else:
        print(f"#{test_case} no")



            
            
            