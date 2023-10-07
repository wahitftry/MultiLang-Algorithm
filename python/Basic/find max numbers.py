num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    max_num = num1
else:
    max_num = num2

print(f"The maximum of {0} and {1} is {2}".format(num1, num2, max_num))