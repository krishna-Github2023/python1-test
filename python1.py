# example.py

def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")
    return result


def multiply_numbers(x, y):
    result = x * y
    print(f"The product of {x} and {y} is: {result}")
    return result


def main():
    num1 = 5
    num2 = 3

    add_result = add_numbers(num1, num2)
    multiply_result = multiply_numbers(num1, num2)

    print(f"Final result: {add_result + multiply_result}")


if __name__ == "__main__":
    main()
