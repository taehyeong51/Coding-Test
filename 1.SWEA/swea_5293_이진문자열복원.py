'''
정보 : 인접한 두 문자 끊어서 봤을 때, 각각 쌍 몇 번씩 등장하는지 적어놓은 것
경우의 수 : 00,01,10,11
0011
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