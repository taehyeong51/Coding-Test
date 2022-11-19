'''
1. 입력받을 문자열을 길이가 50이상 되도록 반복
2. 비교
'''
import sys
sys.stdin = open("1_sample_input.txt", "r")
T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word1,word2 = map(list,input().split())
    
    # 1. 입력받을 문자열을 길이가 50이상 되도록 반복
    cnt = 0
    while len(word1) < 100:
        word1 += word1[cnt%len(word1)]
        cnt += 1
        
    cnt = 0
    while len(word2) < 100:
        word2 += word2[cnt%len(word2)]
        cnt += 1
    # print(len(word1),len(word2))
    # print("".join(word1))
    # print("".join(word2))
    if word1 == word2:
        print(f"#{test_case} yes")
    else:
        print(f"#{test_case} no")