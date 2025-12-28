# --------------------------------------------------------
# Day 27: Recursion (A function calling itself)
# --------------------------------------------------------

# Recursion means a function calls itself until a stopping point.
# That stopping point is called the BASE CONDITION.


# --------------------------------------------------------
# 1. Basic recursive function
# --------------------------------------------------------

def simple_count(n):
    if n == 0:
        print("Reached 0")
        return
    print("n =", n)
    simple_count(n - 1)

print("Simple recursion:")
simple_count(5)



# --------------------------------------------------------
# 2. Factorial using recursion
# --------------------------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1     # base condition
    return n * factorial(n - 1)

print("\nFactorial of 5 =", factorial(5))



# --------------------------------------------------------
# 3. Sum of first n numbers
# --------------------------------------------------------

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print("\nSum of first 5 numbers =", sum_n(5))



# --------------------------------------------------------
# 4. Fibonacci using recursion
# --------------------------------------------------------

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci of 6 =", fibonacci(6))



# --------------------------------------------------------
# 5. Recursion to print a list
# --------------------------------------------------------

def print_list(items, index=0):
    if index == len(items):
        return
    print(items[index])
    print_list(items, index + 1)

print("\nPrinting a list using recursion:")
print_list(["apple", "banana", "mango"])



# --------------------------------------------------------
# 6. Reverse a string using recursion
# --------------------------------------------------------

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print("\nReverse string:", reverse_string("Python"))



# --------------------------------------------------------
# 7. Count digits in a number
# --------------------------------------------------------

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print("\nDigits in 98765:", count_digits(98765))



# --------------------------------------------------------
# 8. Recursion with both printing before and after call
# --------------------------------------------------------

def trace(n):
    if n == 0:
        return
    print("Before:", n)
    trace(n - 1)
    print("After:", n)

print("\nTracing recursion:")
trace(3)



# --------------------------------------------------------
# 9. Real-world Example: Directory structure scanning (simulation)
# --------------------------------------------------------

filesystem = {
    "folder1": ["file1.txt", "file2.txt"],
    "folder2": {
        "projects": ["main.py", "utils.py"],
        "images": ["img1.png"]
    }
}

def explore(fs, level=0):
    for key in fs:
        print("  " * level + str(key))
        if isinstance(fs[key], dict):
            explore(fs[key], level + 1)
        else:
            for item in fs[key]:
                print("  " * (level + 1) + item)

print("\nExploring a fake folder structure:")
explore(filesystem)



# --------------------------------------------------------
# 10. Real-world Example: Binary Search (recursive)
# --------------------------------------------------------

def binary_search(arr, target, low, high):
    if low > high:
        return -1   # not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

nums = [2, 4, 6, 8, 10, 12, 14]
print("\nBinary Search result:", binary_search(nums, 10, 0, len(nums) - 1))



# --------------------------------------------------------
# End of Day 27: Recursion
# --------------------------------------------------------
