def fibonacci_recursive(n):
    """Return the nth Fibonacci number (recursive)."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    """Return the nth Fibonacci number (iterative)."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    print("Fibonacci sequence:")
    print(fibonacci_recursive(10))  # Example usage
    print(fibonacci_iterative(10))  # Example usage
