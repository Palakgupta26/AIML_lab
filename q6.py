fruits=["apple","banana","mango","pineapple","cherry"]
print(f"fruit[0]: {fruits[0]}")
print(f"fruit[4]: {fruits[4]}")
print(f"fruit[-1]: {fruits[-1]}")
print(f"fruit[-2]: {fruits[-2]}")

fruits[1]="watermelon"

print(fruits)

fruits.remove("apple")

print(fruits)

print(len(fruits))

fruits.sort()
print(f"Sorted list: {fruits}")