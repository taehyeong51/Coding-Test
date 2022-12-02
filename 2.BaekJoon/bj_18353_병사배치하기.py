'''
무작위 나열된 N 명의 병사
전투력 높은 병사가 앞쪽에 오도록 내림차순으로 배치
1. 앞쪽 병사 전투력 > 뒤쪽 병사 전투력
2. 특정한 위치 병사 열외
3. 남아있는 병사의 수 최대

Sol.
재배열이 아닌 열외를 통해 남은 병사 최대로 하여 내림차순으로 배열 만들기
'''
N = int(input())
soldiers = list(map(int,input().split()))

cnt = 0
is_done = False

def check():
    global cnt,is_done,soldiers
    is_done = True
    tmp = []
    for i in range(len(soldiers)-1):
        if soldiers[i] < soldiers[i+1]:
            cnt += 1
            is_done = False
        else:
            tmp.append(soldiers[i])
    soldiers = tmp

while not is_done:
    check()
        
print(cnt)
print(soldiers)
'''
5
1 2 3 4 5
4

5
10 5 10 5 10
3
'''

