principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period (in years): "))
compounding = int(input("Enter the number of times the interest is compounded per year: "))
amount = principal * (1 + (rate / compounding)) ** (compounding * time)
interest = amount - principal
print("The compound interest for a principal amount of {0}, an interest rate of {1}%, a time period of {2} years, and compounded {3} times per year is {4}".format(principal, rate, time, compounding, interest))