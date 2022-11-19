import sys
sys.stdin = open("sample_input (2).txt", "r")
from itertools import permutations
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    numbers = list(input())
    candidates = list(permutations(numbers))
    is_possible = False
    for candidate in candidates:
        if int("".join(candidate)) != int("".join(numbers)) and int("".join(candidate)) % int("".join(numbers)) == 0:
            is_possible = True
            break
    if is_possible:
        print(f"#{test_case} possible")
    else:
        print(f"#{test_case} impossible")
    