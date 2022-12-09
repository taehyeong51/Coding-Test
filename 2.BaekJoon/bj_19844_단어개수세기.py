'''
1. - 단위로 구분
2. ce,je,ne,me,te,se,le,la,de,que,si + (a,e,i,o,u,h)이면
    앞 단어 마지막 모음 삭제, ' 붙으면서 이어짐
'''
pre = {'c':'ce','j':'je','n':'ne','m':'me','t':'te',
       's':'se','l':'le','l':'la','d':'de','qu':'que','s':'si'}
post = ['a','e','i','o','u','h']

sentence = input()

def seperate1(_sentence):
    _sentence = list(_sentence.split(" "))
    for i in range(len(_sentence)):
        tmp = _sentence.pop(0)
        if "-" in tmp:
            for w in tmp.split("-"):
                _sentence.append(w)
        else:
            _sentence.append(tmp)
    return _sentence

def seperate2(_sentence):
    if "'" in list(_sentence):
        tmp = _sentence.split("'")
        while '' in tmp:
            tmp.remove('')
        word1,word2 = tmp[0],tmp[1]
        if word1 in list(pre.keys()) and list(word2)[0] in post:
            return True,pre[word1],word2
        else:
            return True,word1+"'"+word2,None
    else:
        return False,_sentence,None
    
def remove1(_sentence):
    for i in range(len(_sentence)):
        while _sentence[i][0] == "'":
            _sentence[i] = _sentence[i][1:]
        while _sentence[i][-1] == "'":
            _sentence[i] = _sentence[i][:-1]
    return _sentence     
       
sentence = remove1(sentence)
sentence = seperate1(sentence)
ans = []

for word in sentence:
    is_seperate,w1,w2 = seperate2(word)
    if is_seperate:
        if w1:
            ans.append(w1) 
        if w2:
            ans.append(w2) 
    else:
        ans.append(w1)

print(len(ans))
# print(ans)