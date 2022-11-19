'''
잡초 자라면서 원래 . 또는 (,) 를 가림
초원에 존재할 수 있었던 공의 개수의 최소값
'''
# import sys
# sys.stdin = open("sample_input (1).txt", "r")
T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    grasses = list(input())
    tmp = []
    for idx,grass in enumerate(grasses):
        if grass == '(' or grass == ')':
            tmp.append((idx,grass))
    cnt = 0
    visited = [0 for _ in range(len(grasses))]
    for idx,grass in tmp:
        if not visited[idx]:
            visited[idx] = 1
            if grass == '(':
                if idx+1 < len(grasses):
                    if (grasses[idx+1] == '|' or grasses[idx+1] == ')') and not visited[idx+1]:
                        visited[idx+1] = 1
                        cnt += 1        
            elif grass == ')':
                if -1 < idx-1:
                    if grasses[idx-1] == '|':
                        cnt += 1
    print(f"#{test_case} {cnt}")
        
    
            