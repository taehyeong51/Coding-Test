S = list(input())

alphabet = ['a','b','c','d','e','f','g','h','i',
            'j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z']
capital_alphabet = ['A','B','C','D','E','F','G','H','I',
                    'J','K','L','M','N','O','P','Q','R','S',
                    'T','U','V','W','X','Y','Z']

for i in range(len(S)):
    if S[i]:
        if S[i] in alphabet:
            S[i] = alphabet[(alphabet.index(S[i])+13)%len(alphabet)]
        elif S[i] in capital_alphabet:
            S[i] = capital_alphabet[(capital_alphabet.index(S[i])+13)%len(alphabet)]
            
print("".join(S))