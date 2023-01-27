numbers = list(map(int,list(input())))

zero = 0
one = 0

is_zero,is_one = False,False

for idx,n in enumerate(numbers):
    if not is_zero and not is_one:
        if n == 1:
            is_one = True
        elif n == 0:
            is_zero = True
        continue
    if is_zero:
        if n == 1:
            is_zero = False
            is_one = True
            zero += 1
    elif is_one:
        if n == 0:
            is_one = False
            is_zero = True
            one += 1
    if idx == len(numbers)-1:
        if not zero and not one:
            continue
        if is_zero:
            zero += 1
        elif is_one:
            one += 1
print(min(zero,one))