#P2-- Dynamic Programming
#Q)-- implement the fibonacci sequence using tabulation (bottom-up Approach)to generate the first N Fibonacci numbers.

def fibonacci(n):
    if n <= 0:
        print("Enter a positive number.")
        return
    dp = [0] * n
    dp[0] = 0
    if n > 1:
        dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    print("Fibonacci Series:", end=" ")
    for i in range(n):
        print(dp[i], end=" ")
n = int(input("Enter the number of terms: "))
fibonacci(n)

