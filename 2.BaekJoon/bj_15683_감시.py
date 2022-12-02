import sys
import copy
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
inf = 99999
N,M = map(int,input().split()) # 세로 N, 가로 M

def transpose(list_):
    return list(map(list,list(zip(*list_))))

# 상하좌우 감시
# 상하좌우 감시
def left(r,c,graph):
    global CCTVs
    graph_ans = copy.deepcopy(graph)

    target = graph_ans[r]
    cnt_6 = target.count(6)
    if cnt_6 == 1:
        idx = target.index(6) if 6 in target else inf
        if 6 in target and idx < c:
            target[idx+1:c] = ['#' for _ in range(len(target[idx+1:c]))]  
        else:
            target[:c] = ['#' for _ in range(len(target[:c]))]
    elif c < M:
        new_target = copy.deepcopy(target)
        new_target[c+1:] = [inf for _ in range(len(new_target[c+1:]))]
        new_target.reverse()
        idx = len(target) - new_target.index(6) - 1 if 6 in new_target else inf
        if 6 in new_target and idx < c:
            target[idx+1:c] = ['#' for _ in range(len(target[idx+1:c]))]
        else:
            target[:c] = ['#' for _ in range(len(target[:c]))]
    graph_ans[r] = target
    for CCTV in CCTVs:
        r,c,n_cctv = CCTV
        graph_ans[r][c] = n_cctv
    for wall in walls:
        r,c,n_wall = wall
        graph_ans[r][c] = n_wall
    return graph_ans
    
def right(r,c,graph):
    graph_ans = copy.deepcopy(graph)
    target = graph_ans[r]
    cnt_6 = target.count(6)
    if cnt_6 == 1:
        idx = target.index(6) if 6 in target else -inf
        if 6 in target and idx > c:
            target[c+1:idx] = ['#' for _ in range(len(target[c+1:idx]))]
        else:
            target[c+1:] = ['#' for _ in range(len(target[c+1:]))]
    elif c < M:
        new_target = copy.deepcopy(target)
        new_target[:c] = [inf for _ in range(len(new_target[:c]))]
        idx = new_target.index(6) if 6 in new_target else inf
        if 6 in new_target and idx > c:
            target[c:idx] = ['#' for _ in range(len(target[c:idx]))]
        else:
            target[c:] = ['#' for _ in range(len(target[c:]))]
    graph_ans[r] = target
    for CCTV in CCTVs:
        r,c,n_cctv = CCTV
        graph_ans[r][c] = n_cctv
    for wall in walls:
        r,c,n_wall = wall
        graph_ans[r][c] = n_wall
    return graph_ans
    
def up(r,c,graph):
       
    graph_transpose = transpose(graph)
    target = graph_transpose[c]
    cnt_6 = target.count(6)
    if cnt_6 == 1:
        idx = target.index(6) if 6 in target else -inf
        if 6 in target and idx < r:
            target[idx+1:r] = ['#' for _ in range(len(target[idx+1:r]))]
        else:
            target[:r] = ['#' for _ in range(len(target[:r]))]
    elif r < N:
        new_target = copy.deepcopy(target)
        new_target[r:] = [inf for _ in range(len(new_target[r:]))]
        new_target.reverse()
        idx = len(target) - new_target.index(6) - 1 if 6 in new_target else inf
        if 6 in new_target and idx < r:
            target[idx+1:r] = ['#' for _ in range(len(target[idx+1:r]))]
        else:
            target[:r] = ['#' for _ in range(len(target[:r]))]
    graph_transpose[c] = target
    graph_ans = transpose(graph_transpose)
    
            
    for CCTV in CCTVs:
        r,c,n_cctv = CCTV
        graph_ans[r][c] = n_cctv
    for wall in walls:
        r,c,n_wall = wall
        graph_ans[r][c] = n_wall
    return graph_ans
    
def down(r,c,graph):
    graph_transpose = transpose(graph)

    target = graph_transpose[c]
    cnt_6 = target.count(6)
    if cnt_6 == 1:   
        idx = target.index(6) if 6 in target else inf
        if 6 in target and idx > r:
            target[r+1:idx] = ['#' for _ in range(len(target[r+1:idx]))]
        else:
            target[r+1:] = ['#' for _ in range(len(target[r+1:]))]
    elif r < N:
        new_target = copy.deepcopy(target)
        new_target[:r] = [inf for _ in range(len(new_target[:r]))]
        idx = new_target.index(6) if 6 in new_target else inf
        if 6 in new_target and idx > r:
            target[r+1:idx] = ['#' for _ in range(len(target[r+1:idx]))]
        else:
            target[r+1:] = ['#' for _ in range(len(target[r+1:]))]
        
    graph_transpose[c] = target
    graph_ans = transpose(graph_transpose)
    
    for CCTV in CCTVs:
        r,c,n_cctv = CCTV
        graph_ans[r][c] = n_cctv
    for wall in walls:
        r,c,n_wall = wall
        graph_ans[r][c] = n_wall

    return graph_ans

# 영역 count
def cnt(graph_):
    global N,M
    ans = 0
    for r in range(N):
        for c in range(M):
            if graph_ is not None:
                if graph_[r][c] == 0:
                    ans += 1
    return ans
            
def watching_area(CCTVs,v,graph):
    global ans
    if v == len(CCTVs):
        if cnt(graph) < ans:
            ans = cnt(graph)
        return
    cctv = CCTVs[v]
    r,c,n = cctv
    graph_o = copy.deepcopy(graph)
    graph_tmp2 = None
    rotate = 1
    if n == 1: # 4번
        graph = left(r,c,graph_o)
        watching_area(CCTVs,v+1,graph)
        
        graph = right(r,c,graph_o)
        watching_area(CCTVs,v+1,graph)
        
        graph = up(r,c,graph_o)
        watching_area(CCTVs,v+1,graph)
        
        graph = down(r,c,graph_o)
        watching_area(CCTVs,v+1,graph)
        
    elif n == 2: # 2번

        graph = right(r,c,left(r,c,graph_o))
        watching_area(CCTVs,v+1,graph)
        
        graph = up(r,c,down(r,c,graph_o))
        watching_area(CCTVs,v+1,graph)
        
    elif n == 3: # 4번
        graph = up(r,c,right(r,c,graph_o))
        watching_area(CCTVs,v+1,graph)
        
        graph = right(r,c,down(r,c,graph_o))
        watching_area(CCTVs,v+1,graph)
        
        graph = left(r,c,down(r,c,graph_o))
        watching_area(CCTVs,v+1,graph)
        
        graph = left(r,c,up(r,c,graph_o))
        watching_area(CCTVs,v+1,graph)
    elif n == 4: # 4번
        graph = left(r,c,up(r,c,right(r,c,graph_o)))
        watching_area(CCTVs,v+1,graph)
        
        graph = up(r,c,right(r,c,down(r,c,graph_o)))
        watching_area(CCTVs,v+1,graph)
        
        graph = right(r,c,down(r,c,left(r,c,graph_o)))
        watching_area(CCTVs,v+1,graph)
        
        graph = down(r,c,left(r,c,up(r,c,graph_o)))
        watching_area(CCTVs,v+1,graph)
        
    elif n == 5: # 0번
        graph = left(r,c,(up(r,c,right(r,c,(down(r,c,graph_o))))))
        watching_area(CCTVs,v+1,graph)    
        
# CCTV : 1 ~ 5, 벽 : 6
graph = [list(map(int,input().split())) for _ in range(N)]

CCTVs = []
walls = []
# graph 돌면서 CCTV 위치 저장
for r in range(N):
    for c in range(M):
        if graph[r][c] != 0 and graph[r][c] != 6:
            CCTVs.append((r,c,graph[r][c]))
        elif graph[r][c] == 6:
            walls.append((r,c,graph[r][c]))

# initialize
ans = 99999999

# CCTV 위치 돌면서 해당 위치, 재귀로 해결해야 함

watching_area(CCTVs,0,graph)
    
print(ans)
