#RevoU Mini Course - Phyton Code Challenge

# from the given list below:
product = ["Apple", "Orange", 100, "Grape", 120.33, "Cherry", 13.00, "Pear", 500, "Melon", "Strawberry"]

# Create separate lists of strings and numbers
str_items = []
num_items = []

for item in product:
    if isinstance(item, str):
        str_items.append(item)
    elif isinstance(item,int) or isinstance(item,float):
        num_items.append(item)

print(str_items)
print(num_items)

# Sort the strings list in ascending order
str_items.sort()
print(str_items)

# Sort the strings list in descending order
str_items.sort(reverse=True)
print(str_items)

# Sort the number list from lowest to highest
num_items.sort()
print(num_items)

# Sort the number list from highest to lowest
num_items.sort(reverse=True)
print(num_items)