'''
구두점 : ".", "?", "!"
마지막 단어 - 구두점으로 끝남
이름 : 대문자로 시작, 소문자로 끝

'''
import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

Capital = ['A','B','C','D','E','F','G','H','I','J','K',
           'L','M','N','O','P','Q','R','S','T','U',
           'V','W','X','Y','Z']
Letters = ['a','b','c','d','e','f','g','h','i','j','k',
           'l','m','n','o','p','q','r','s','t','u',
           'v','w','x','y','z']
for test_case in range(1, T + 1):
    N = int(input())
    text = list(input())
    list_text = []
    j = 0
    for i in range(len(text)):
        if text[i] == "!" or text[i] == "?" or text[i] == ".":
            list_text.append(text[j:i])
            j = i+1
    answer = [0 for _ in range(N)]
    for idx,text in enumerate(list_text):
        words = list("".join(text).split(" "))
        for word in words:
            word = list(word)
            if word and word[0] in Capital:
                if len(word) == 1:
                    answer[idx] += 1
                else:
                    small = True
                    for alphabet in word[1:]:
                        if alphabet in Letters:
                            continue
                        else:
                            small = False
                            break
                    if small:
                        answer[idx] += 1
    # print(answer)
    answer = " ".join(list(map(str,answer)))
    print(f"#{test_case} {answer}")
            
    
            
            
            