

# AI Generated Fix:
def search_info(name):
    if name in Contact:
        print(f"The number of {name} is {Contact[name]}")
    else:
        print(f"{name} is not found")

def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):  # Corrected loop to iterate up to n (inclusive)
            result *= i
        return result

def add_info(name, number):
    Contact[name] = number
    print(f"Added {name} with number {number}")

def deletetask(task):
    try:
        tasks.remove(task)
        print(f"{task} removed from tasks")
    except ValueError:
        print(f"{task} not found in tasks")

Contact = {}
tasks = []