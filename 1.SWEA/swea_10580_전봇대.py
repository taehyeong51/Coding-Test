'''
전봇대에 총 몇 개의 교차점?
input
1. TC
2. 전선 개수 N
3. N개의 줄에 A_i, B_i

Sol.
j번째 A_j와 B_j가 이전 모든 0~j-1번째와 비교하여 시작점 끝점 크기 비교
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
    
for test_case in range(1, T + 1):
    N = int(input())
    lines = []
    for _ in range(N):
        A,B = map(int,input().split())
        lines.append((A,B))
    cnt = 0
    for i in range(N):
        A,B = lines[i]
        for j in range(0,i):
            old_A,old_B = lines[j]
            if A < old_A and B > old_B:
                cnt += 1
            elif A > old_A and B < old_B:
                cnt += 1
    print(f"#{test_case} {cnt}")
            
    
            
            
            