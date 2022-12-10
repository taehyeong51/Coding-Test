n = int(input())
dp = [0 for _ in range(91)]
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 3

def fibonacci(n):
    if n == 0:
        return 0
    if dp[n]:
        return dp[n]
    else:
        if dp[n-1]:
            n_1 = dp[n-1]
        else:
            n_1 = fibonacci(n-1)
        if dp[n-2]:
            n_2 = dp[n-2]
        else:
            n_2 = fibonacci(n-2)
        dp[n] = n_1+n_2
        return n_1 + n_2
    
print(fibonacci(n))

