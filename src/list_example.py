print("""
----------------------------------------------

LIST

- ordered collection of objects
- store and fetch by positional offset (0, 1, 3, ...)
- nested to arbitrary depth
- value can be updated (mutable)

----------------------------------------------
\n\n\n""")


print("""
----------------------------------------------

CREATE A LIST

Syntax:

    list_identifier = [ item0 , item1, item2 ]

           index    0       1      2

Note:
 - item (any data type including custom class object) separated by comma
 - access by offset start from index 0

Example:
""")

a_list = ['a', 5, 6.7, 'hi']

print("a_list = ['a', 5, 6.7, 'hi']")
print("a_list:", a_list)



print("""
----------------------------------------------

SIZE OF LIST

Syntax:

   size = len(list_identifier)

Example:
""")

a_list = ['a', 5, 6.7, 'hi']

print("Number of items in a_list:", len(a_list))



print("""
----------------------------------------------

FETCH ALL ITEMS

Syntax:

 for item in list_identifier:
    # do something with item

Example:
""")

a_list = ['a', 5, 6.7, 'hi']

print("items in a_list:")
for item in a_list:
    print(item)



print("""
----------------------------------------------

FETCH ITEM

Syntax:

    item = list_identifier[index]

Example:
""")


a_list = ['a', 5, 6.7, 'hi']

print('a_list:', a_list)

print('Fist item:', a_list[0])
print('Last item:', a_list[len(a_list)-1])



print("""
----------------------------------------------

UPDATE ITEM

Syntax:

    list_identifier[index] = new_value

Example:
""")

a_list = ['a', 5, 6.7, 'hi']
print('a_list:', a_list)


new_value = 4
print("Replace first item in a_list with", new_value)

a_list[0] = new_value

print('a_list', a_list)


print("""
----------------------------------------------

ADD ITEM

Syntax:

    A)  list_identifier.insert(index, new_item)
    B)  list_identifier.append(new_item)

Note
    A) Add new item to desired position in list
    B) Add new item to end of list

Example:
""")

a_list = ['a', 5, 6.7, 'hi']
print('a_list', a_list)

print('Option A) append')
a_list.append("Peter")
print('a_list', a_list)


print('Option B) insert')
a_list.insert(0, "Peter")
print('a_list', a_list)


print("""
Merge List

Syntax:

    new_list = list_identifier + list_identifier_2

Example:
""")


numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7, 8]

print('numbers_1:', numbers_1)
print('numbers_2:', numbers_2)

numbers = numbers_1 + numbers_2
print('numbers:', numbers)


print("""
----------------------------------------------

DELETE ITEM

Syntax:

    A)  del list[index]
    B)  list.remove(item)
    C)  item = list.pop(index)

Example:
""")

a_list = [1, "2", 3.5, "a"]
print("a_list:", a_list)

print("Option A) Delete")
del a_list[0]
print("a_list:", a_list)

print("Option B) Remove")
a_list.remove("a")
print("a_list:", a_list)

print("Option C) Pop")
item = a_list.pop(-1)
print("a_list:", a_list)
print("item:", item)


print("""
----------------------------------------------

REMOVE ALL ITEMS

Syntax:

    list.clear()

Example:
""")

a_list = [1, "2", 3.5, "a"]
print("a_list:", a_list)

a_list.clear()
print("a_list:", a_list)

























































#
# # Join list into a single string
# a_list = ["1", "2", "3", "4"]
#
# print(a_list)
# print(" ".join(a_list))
#
# # slice
# # Get part of a list
#
# # create a new list from a existing list
# # new list contains element 1 to last element -1  of existing list
# sub_list = a_list[1:-1]
# print(sub_list)
#
# # create a new list from a existing list
# # new list contains element 2 to end of list
# sub_list_2 = a_list[2:]
# print(sub_list_2)
#
# # create a new list from a existing list
# # new list contains element 1 to last element, at step of 2
# sub_list_2 = a_list[0::2]
# print(sub_list_2)
#
# # loop through element based on index
# names = ["Peter", "John", "Jeff", "Donald", "Adams", "Jackson"]
# for i in range(len(names)):
#     print("Names {}: {}".format(i + 1, names[i]))
#
# # join list of string with comma
# print("Here's your list:")
# new_list = ', '.join(names)
# print("{}".format(new_list))
#
# # if it contains non-string types (such as integers, floats, bools, None) then do:
# floats = [3.0, 4.5, 6.6, 7.89]
# new_list = ','.join(map(str, floats))
# print(new_list)
#
# # convert a list into a string and remove brace
# integers = [1, 2, 3, 4]
# integers_str = str(integers)
# integers_str_without_brace = integers_str.strip("[]")
# print(integers_str_without_brace)
#
#
# # more on slice
# # https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
#
