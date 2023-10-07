def is_armstrong(num_str):
    num_digits = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_digits
    
    return sum == int(num_str)

num_str = input("Enter a number: ")
if is_armstrong(num_str):
    print("{0} is an Armstrong number".format(num_str))
else:
    print("{0} is not an Armstrong number".format(num_str))