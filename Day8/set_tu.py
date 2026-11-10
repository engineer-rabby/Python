fruits = {"guava", "banana", "mango", "apple", "orange"}

print(type(fruits))

print("guava" in fruits)

print("grapes" not in fruits)

setone = {"guava", "banana", "mango", "apple", "orange"}
settwo = {"grapes", "banana", "mango", "kiwi", "orange"}

setone.update(settwo)

print(setone)