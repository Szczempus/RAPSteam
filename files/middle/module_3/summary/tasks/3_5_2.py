
# Global dictionary to store computed Fibonacci values
memo = {}

def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    return memo[n]

# Example usage:
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci number at position {n} is {fibonacci_memo(n)}")
