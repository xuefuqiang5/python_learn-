from unicodedata import name

my_dict = {1:11,2:22, 3:33}
new_value = 44


l = set()
l1 = {}
print(type(l), type(l1))

my_set = {1, 1, 3, 6, 8}
print(my_set)
my_set2 = {1, 7, 5, 7, 4}
print(my_set2)
my_set3 = my_set2|my_set
print(my_set3)

# Find the presence of characters in the rang 32 ~ 256 whose names contain "SIGN"
# set comprehension 
my_set = {chr(i) for i in range(32, 256) if "SIGN" in name(chr(i), '')}
print(my_set)

set_itrator = my_set.__iter__()
for item in set_itrator:
    print(item, end = "\n")


# The "in" operator in Python 
my_string = "hello, world!"
print("hello" in my_string)