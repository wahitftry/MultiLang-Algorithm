def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_digits
    
    if sum == num:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_armstrong(num):
    print("{0} is an Armstrong number".format(num))
else:
    print("{0} is not an Armstrong number".format(num))