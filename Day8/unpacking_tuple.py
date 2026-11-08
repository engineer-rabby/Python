a_tuple = (1, 2, 3, 4, 5)

print(a_tuple[0])  # Output: 1

a, b, c, d, e = a_tuple  # This will unpack the tuple into individual variables.
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: 4
print(e)  # Output: 5

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)