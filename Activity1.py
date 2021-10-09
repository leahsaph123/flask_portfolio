#                1       2      3      4       5      6      7
student_list = ['pam', 'rob', 'joe', 'greg', 'bob', 'amy', 'matt']

# The following print statement includes elements at index 2 & excludes element at index 5
print(student_list[2:5])

# print beginning to 4th
print(student_list[:-5])


# MY OWN WORK STARTS HERE


# print elements 6th to end (index 5)
print(student_list[:6-7])

# print elements beginning to end
print(student_list[:1-7])

# check if rob is in the student_list
if 'rob' in student_list:
    print('Yes, rob is in the list')


p1 = {"name": "John", "age": 61, "city": "Eugene"}
p2 = {"name": "Risa", "age": 16, "city": "New York"}
p3 = {"name": "Ryan", "age": 16, "city": "Los Angeles"}
p4 = {"name": "Shekar", "age": 16, "city": "San Francisco"}

# a list of dictionaries
list_of_people = [p1, p2, p3, p4]

# write some code to Print List of people one by one
print(list_of_people[:1-4])
