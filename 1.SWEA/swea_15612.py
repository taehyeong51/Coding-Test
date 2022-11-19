'''
1. 8개의 룩
2. 모든 룩은 서로 공격 x = 서로 다른 두 룩은 같은 열 or 행 X
'''
from collections import deque
T = int(input())

# def check_1():
#     global graph
#     cnt = 0
#     for r in range(8):
#         for c in range(8):
#             if graph[r][c]=='O':
#                 cnt += 1
#             if cnt > 8:
#                 return False
#     return True

def check():
    global graph
    cnt = 0
    dr = [-1,1]
    dc = [-1,1]
    for r in range(8):
        for c in range(8):
            if graph[r][c] == 'O':
                cnt += 1
                visited = [[0]*8 for _ in range(8)]
                q = deque()
                q.append((r,c))
                visited[r][c] = 1
                # 세로 방향
                while q:
                    rr,cc = q.popleft()
                    # print(f"세로에서 rr,cc:({rr},{cc}), graph[rr][cc] = {graph[rr][cc]}")
                    
                    for i in range(2):
                        nr = rr + dr[i]
                        if 0 <= nr < 8 and visited[nr][cc] == 0:
                            if graph[nr][cc] == 'O':
                                return False
                            visited[nr][cc] = 1
                            q.append((nr,cc))
                # 가로 방향
                q.append((r,c))
                while q:
                    rr,cc = q.popleft()
                    # print(f"가로에서 rr,cc:{rr},{cc}, graph[rr][cc] = {graph[rr][cc]}")
                    
                    for i in range(2):
                        nc = cc + dc[i]
                        if 0 <= nc < 8 and visited[rr][nc] == 0:
                            if graph[rr][nc] == 'O':
                                return False
                            visited[rr][nc] = 1
                            q.append((rr,nc))
    if cnt == 8:
        return True
                
        
    
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    graph = [list(input()) for _ in range(8)]
    if check():
        print(f"#{test_case} yes")
    else:
        print(f"#{test_case} no")
    # ///////////////////////////////////////////////////////////////////////////////////

