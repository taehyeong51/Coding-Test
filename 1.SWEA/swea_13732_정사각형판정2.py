'''
NxN 격자판
'.' : 비어있음
'#' : 막혀있음
이때 막혀있는 칸들이 하나의 정사각형 이루는지 판단

Sol.
1. graph의 #가 존재하는 위치 모두 가져옴
2. bfs를 통해 #의 길이만큼 돌면서 만약 #가 아니면 No return
'''

from collections import deque

T = int(input())
def check(blocks,graph):
    if not blocks:
        return "no"
    l = len(blocks) ** (1/2)
    if l % 1 != 0: # 제곱수가 아니면
        return "no"
    l = int(l)
    i_r,i_c = map(int,blocks.popleft())
    for r in range(i_r,i_r+l):
        for c in range(i_c,i_c+l):
            if graph[r][c] != "#":
                return "no"
    return "yes"

for tc in range(1,T+1):
    N = int(input())
    graph = [list(input()) for _ in range(N)]
    blocks = deque((r,c) for r in range(N) for c in range(N) if graph[r][c] == '#')
    answer = check(blocks,graph)
    print(f"#{tc} {answer}")