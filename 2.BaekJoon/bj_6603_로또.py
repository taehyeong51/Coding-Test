from itertools import combinations
first = True
while True:
    numbers = list(map(int,input().split()))
    k = numbers[0]
    if k == 0:
        break
    numbers = numbers[1:]
    p_numbers = sorted(list(combinations(numbers,6)))
    
    if not first:
        print("")
        
    for p_number in p_numbers:
        for n in p_number:
            print(n,end=" ")
        print("")
    first = False
    