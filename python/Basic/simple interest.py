principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period (in years): "))
interest = (principal * rate * time) / 100
print("The simple interest for a principal amount of {0}, an interest rate of {1}%, and a time period of {2} years is {3}".format(principal, rate, time, interest))