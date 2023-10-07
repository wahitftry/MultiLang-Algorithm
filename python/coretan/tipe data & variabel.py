print("=====VARIABEL=====")

number = 10
print(number)

number = 100
print(number)

number = 0.1
print(number)

email = "wahitfitriyanto@gmail.com"
print(email)

number1, number2, email = 10, 0.1, "wahitfitriyanto@gmail.com"
print(number1)
print(number2)
print(email)

number1 = number2 = number3 = 100
print(number1)
print(number2)
print(number3)

PI = 3.14
GRAVITY = 9.8

variable_name = "indonesia AI 1"
VARIABLE_NAME = "Indonesia AI 2"

biner_number = 0b1010
decimal_number = 100
float_number = 1.5e2

print(float_number)

print("\n=====TIPE DATA=====")

a = 5
print(type(a))

b = 3.0
print(type(b))

c = 4 / 5
print(type(c))

c = a + b
print(type(c))

a = float(a)
print(type(a))

c = int(4 / 5)
print(type(c))
print(c)

a = str(a)
print(a)

print("\n=====DIFFERENT METHOD=====")

c = 8 / 5
c = c.__ceil__()
print(c)

c = 8 / 5
c = c.__float__()
print(c)

print("\n=====STRING=====")

s = "this is single-line string"
print(type(s))

s = """this is string
but not single line, this multi-line 
"""
print(type(s))

s = "This is Single-Line String"
s = s.lower()
print(s)

s = "This is Single-Line String"
s = s.upper()
print(s)

s = "This is Single-Line String"
s = s.replace("is", "of")
print(s)

name = "Wahit"
s = f"my name is {name}"
print(s)

print("\n=====BINARY=====")
b = True
print(type(b))
print(type(b == 1))

print(b == 1)
print(b == 0)

print(False and True)
print(False or True)

print("\n=====SEQUENCE TYPE=====")
print("=====List, Tuple and Dictionary=====")

l = [1, 2.2, "python"]
print(type(l))

t = (5, "program", 1 + 3)
print(type(t))

d = {"key": "value", "key2": "value"}
print(type(d))
