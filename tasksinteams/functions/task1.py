def calculation_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculation_factorial(n - 1)

number = int(input())
result = calculation_factorial(number)
print(f"factorial of number {number} equals to {result}")