print("""
----------------------------------------------

TUPLE

- ordered collection of objects
- store and fetch by positional offset (0, 1, 3, ...)
- nested to arbitrary depth
- value cannot be updated (immutable)

----------------------------------------------
\n\n\n""")


print("""
----------------------------------------------

CREATE

Syntax:

    A) tuple_name = (item0 , item1, item2)

    B) tuple_name = item0 , item1, item2

             index    0       1      2

Note:
 - item (any data type including custom class object) separated by comma
 - access by offset start from index 0

Example:
""")

tuple_1 = (1, 2.5, "a")
print("tuple_1:", tuple_1)

tuple_2 = 1, 6.7, "c"
print("tuple_2:", tuple_2)

print("""
----------------------------------------------

SIZE

Syntax:

   size = len(tuple)

Example:
""")


tuple_1 = (1, 2.5, "a")
print("tuple_1:", tuple_1)

size = len(tuple_1)
print("Number of items in tuple_1:", size)


print("""
----------------------------------------------

FETCH ITEM

Syntax:

    item = tuple[index]

Example:
""")

tuple_1 = (1, 2.5, "a")
print("tuple_1:", tuple_1)

print("First item:", tuple_1[0])
print("Last item:", tuple_1[len(tuple_1)-1])


print("""
----------------------------------------------

FETCH ALL ITEMS

Syntax:

 for item in tuple_identifier:
    # do something with item

Example:
""")

tuple_1 = (1, 2.5, "a")
print("tuple_1:", tuple_1)

print("Fetch all items in tuple_1:")
for item in tuple_1:
    print(item)


print("""
----------------------------------------------

MERGE

Syntax:

    new_tuple = tuple_1 + tuple_2

Example:
""")

tuple_1 = (1, 2.5, "a")
print("tuple_1:", tuple_1)

tuple_2 = 9, 4, "hu"
print("tuple_2:", tuple_2)

a_tuple = tuple_1 + tuple_2
print("a_tuple:", a_tuple)
