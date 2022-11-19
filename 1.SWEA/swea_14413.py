'''
N x M 격자, N - 행, M - 열
모든 칸 체스판처럼 칠할 수 있는지 검사
"#" : 검은색
"." : 흰색
"?" : 검or흰 <- 선택
'''
# import sys
# sys.stdin = open("sample_input (1).txt", "r")
T = int(input())

from collections import deque

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    graph = [list(input()) for _ in range(N)]
    
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    
    q = deque()
    for r in range(N):
        for c in range(M):
            if graph[r][c] != "?":
                q.append((r,c))
                break
        else:
            continue
        break
    p_im = True

    if graph[r][c] == '#':
        if (r+c)%2 == 0: # "#"가 위치하는 i,j의 합이 짝수였으면
            for r in range(N):
                for c in range(M):
                    if (r+c)%2==0:
                        if graph[r][c] == '.':
                            p_im = False
                            break
                    else:
                        if graph[r][c] == '#':
                            p_im = False
                            break
                    
        else: # "#"가 위치하는 i,j의 합이 홀수였으면
            for r in range(N):
                for c in range(M):
                    if (r+c)%2!=0:
                        if graph[r][c] == '.':
                            p_im = False
                            break
                    else:
                        if graph[r][c] == '#':
                            p_im = False
                            break
    elif graph[r][c] == '.':
        if (r+c)%2 == 0:
            for r in range(N):
                for c in range(M):
                    if (r+c)%2==0:
                        if graph[r][c] == '#':
                            p_im = False
                            break
                    else:
                        if graph[r][c] == '.':
                            p_im = False
                            break
        else:
            for r in range(N):
                for c in range(M):
                    if (r+c)%2!=0:
                        if graph[r][c] == '#':
                            p_im = False
                            break
                    else:
                        if graph[r][c] == '.':
                            p_im = False
                            break
            
    if p_im:
        print(f"#{test_case} possible")
    else:
        print(f"#{test_case} impossible")
        
    
            