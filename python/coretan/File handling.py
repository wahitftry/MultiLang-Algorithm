print("\n======File Handling======")
print("===READ===")

data = open("./data.txt", mode="r", encoding="utf-8")
print(data.read())

string = data.read()
string = string.replace("adalah", "merupakan")
print(string)

print("\n====APPEND====")

data = open("./data.txt", mode="a", encoding="utf-8")
data.write("\nYuk belajar bahasa pemgrograman Python!")

data.close()

print("\n====WRITE====")

data = open("./data.txt", mode="w", encoding="utf-8")
data.write("\nYuk belajar bahasa pemgrograman Python")
data.write("\nSering Latihan supaya Jago")

data.close()

print("\n====BETTER PRATICE====")

print("\n====BEST PRACTICE====")
