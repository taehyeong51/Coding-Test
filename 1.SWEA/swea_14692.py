'''

'''
import sys
sys.stdin = open("sample_input (1).txt", "r")
T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    L = int(input())
    if L % 2 == 0:
        print(f"#{test_case} Alice")
    else:
        print(f"#{test_case} Bob")
    
        
    
            