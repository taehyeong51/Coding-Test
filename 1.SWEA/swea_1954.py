'''
1일때 1
2일때 2,1,1
3일때 3,2,2,1,1
4일때 4,3,3,2,2,1,1
5일때 5,4,4,3,3,2,2,1,1,
-> N만 한번, 나머지 숫자는 두번 씩 반복
'''
import sys
sys.stdin = open("input.txt", "r")
T = int(input())

dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    array = [N-1]
    graph = [[0]*N for _ in range(N)]
    for i in range(N-1,0,-1):
        array.append(i)
        array.append(i)
    r,c = 0,0
    graph[r][c] = 1
    snail = 2
    d = 0
    for n in array:
        for i in range(n):
            r += dr[d%4]
            c += dc[d%4]
            graph[r][c] = snail
            snail += 1
        d += 1
    print(f"#{test_case}")

    for row in graph:
        print(*row)
    # for r in range(N):
    #     for c in range(N):
    #         print(graph[r][c],end=" ")
    #     print("")
            
            
            