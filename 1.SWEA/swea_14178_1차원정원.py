'''
1차원 수직선 위에 정원
좌표 i에 꽃 하나씩 심겨 있음, -> 총 N개의 꽃
자동 분무기 : 정수 좌표에 놓을 수 있음, 좌표 x에 놓여있을 경우, [x-D,x+D] 범위에 분사 가능
N,D 주어질 때, 모든 꽃이 한 개 이상의 분무기에서 물을 받을 수 있도록 하는 최소한의 분무기 수
N : 구간, D : 분사 범위
실제 분사 범위 = 2*D - 1
'''
from math import ceil
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,D = map(int,input().split())
    print(f"#{test_case} {ceil(N/(D*2+1))}")