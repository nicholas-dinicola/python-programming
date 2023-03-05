a_list = []
for x in range(10):
    a_list.append(x**2)

print(a_list)

# Create a list of squares using a list comprehension
squares = [x**2 for x in range(10)]

# Print the list of squares
print(squares)


# Create a dictionary of fruit names and their lengths using a dictionary comprehension
fruits = ["apple", "banana", "watermelon"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}

# Print the dictionary of fruit names and their lengths
print(fruit_lengths)