first_list = [1, 2, 3, 4, 5]

second_list = [2,4,6,8,10]

for i in first_list:
    for j in second_list:
        if i == j:
            print(f"Match found: {i}")