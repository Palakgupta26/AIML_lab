my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_list[2] = 26
print("Modified list: ",my_list)
try:
    my_tuple[2] = 26
except TypeError as e:
    print("Error: ",e)
print("Original tuple: ",my_tuple)

