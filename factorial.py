def factorial(n):
    """Returns the factorial of a number."""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n):
        result *= i
    return result

# Example usage:
print(factorial(5))
