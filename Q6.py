#String example:
my_string = "Hello"
print("Original String:", my_string)
try:
    my_string[0] = 'J'
except TypeError as e:
    print("Error:", e)
#List example:
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
my_list[0] = 10
print("Modified List:", my_list)