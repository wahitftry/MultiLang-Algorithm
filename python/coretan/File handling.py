print("\n======File Handling======")
print("===READ===")

with open("./data.txt", mode="r", encoding="utf-8") as data:
    print(data.read())

    string = data.read()
    string = string.replace("adalah", "merupakan")
    print(string)

print("\n====APPEND====")

with open("./data.txt", mode="a", encoding="utf-8") as data:
    data.write("\nYuk belajar bahasa pemgrograman Python!")

print("\n====WRITE====")

with open("./data.txt", mode="w", encoding="utf-8") as data:
    data.write("\nYuk belajar bahasa pemgrograman Python")
    data.write("\nSering Latihan supaya Jago")

print("\n====BETTER PRATICE====")

with open("./data.txt", mode="r", encoding="utf-8") as data:
    for line in data:
        print(line.strip())

print("\n====BEST PRACTICE====")
