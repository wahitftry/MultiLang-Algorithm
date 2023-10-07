def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** num_digits
    
    return bool(total == num)

num = int(input("Enter a number: "))
if is_armstrong(num):
    print("{0} is an Armstrong number".format(num))
else:
    print("{0} is not an Armstrong number".format(num))