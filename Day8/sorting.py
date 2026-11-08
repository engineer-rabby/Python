my_list = [10, 50, 70, 20, 40, 30]

def my_function(n):
    return abs(n-50)

my_list.sort(key = my_function)

print(my_list)