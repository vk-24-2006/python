my_set = {"apple", "banana", "cherry","apple"}
print(my_set)
print(type(my_set))
new_set = {"apple", "banana", "cherry", False, 0, 1, 2}
print(new_set)
for x in new_set:
    print(x)
print("apple" not in new_set)
new_set.add("orange")
print(new_set)
fruits = {"pineapple","pappaya","kiwi"}
new_set.update(fruits)
print(new_set)
new_set.remove("pineapple")
print(new_set)
new_set.discard("cherry")
print(new_set)