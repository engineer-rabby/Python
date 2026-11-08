fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])  # Output: apple

print("apple" in fruits)  # Output: True

print(fruits[-4:-2])  # Output: ['banana', 'cherry', 'date']

# changing list values
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

# adding new values to the list
fruits.append("fig")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']

fruits.insert(2, "grape")
print(fruits)  # Output: ['apple', 'blueberry', 'grape', 'cherry', 'date', 'elderberry', 'fig']
