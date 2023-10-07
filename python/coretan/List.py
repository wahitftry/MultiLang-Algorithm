print("======LIST======")

list1 = ["apel", "pisang", "melon"]
list2 = [2, 1, 2, 7, 4, 10]
list3 = [True, False, False]
list4 = ["abc", 10, True, 40, "male"]

list5 = [list4, list3, list2, list1]

print(list1 + list2)

list2.sort()

print(list2)

list2.reverse()

print(list2)

list3 = list2.copy()

print(list3.count(2))

fruit_list = ["apple", "banana", "watermelon", "orange", "mango"]

print(fruit_list[-3:])

fruit_list[2] = "avocado"
print(fruit_list)

print("\n====Member List====")

print("apple" in fruit_list)
print("apple" not in fruit_list)

fruit_list = ["apple", "banana", "watermelon"]

print(fruit_list)

fruit_list.insert(1, "orange")

print(fruit_list)

fruit_list1 = [
    "apple",
    "banana",
]
fruit_list2 = [
    "apple",
    "watermelon",
]

fruit_list1.extend(fruit_list2)

print(fruit_list1)

print("\n====List untuk Remove====")

fruit_list = ["apple", "orange", "banana", "watermelon"]
fruit_list.remove("orange")

print(fruit_list)

fruit_list = ["apple", "orange", "banana", "watermelon"]
fruit_list.pop(2)

print(fruit_list)

fruit_list = ["apple", "orange", "banana", "watermelon"]
del fruit_list[1]

print(fruit_list)

fruit_list.clear()

print(fruit_list)
