def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def main():
    num = int(input("Enter a number: "))
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}")


if __name__ == "__main__":
    main()