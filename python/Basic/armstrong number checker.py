def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** num_digits
    
    return bool(total == num)

def main():
    num = int(input("Enter a number: "))
    if is_armstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")


if __name__ == '__main__':
    main()
