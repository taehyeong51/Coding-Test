from collections import defaultdict
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    input()
    numbers = defaultdict(int)
    scores = list(map(int,input().split()))

    for i in range(1000):
        numbers[scores[i]] += 1
    numbers = sorted(list(numbers.items()),key=lambda x : (x[1],x[0]),reverse=True)
    print(f"#{test_case} {numbers[0][0]}")
    # ///////////////////////////////////////////////////////////////////////////////////