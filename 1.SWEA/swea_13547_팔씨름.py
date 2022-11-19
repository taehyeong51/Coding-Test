'''
15번까지 경기 진행했을 때, 8번 이상 이기면 점심 면제, 소정 승 - o, 소정 패 - x
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    score = list(input())
    win = score.count("o")
    l = len(score)
    if 15-l+win >= 8:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")
