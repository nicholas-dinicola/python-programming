numbers = [1, 2, 3, 4, 5]

# Use map() and a lambda function to square numbers
squared = map(lambda x: x**2, numbers)
print(list(squared))

# Use filter() and a lambda function to filter out odd numbers
even_numbers = list(filter(lambda x: x % 2==0, numbers))

print(even_numbers)
