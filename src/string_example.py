print(r"""
----------------------------------------------

DECLARE A STRING

Syntax:

 A) string_name = 'string value'
 B) string_name = "string value"

Example:
""")

string_1 = "Shop"
print("string_1:", string_1)

string_2 = 'Restaurant'
print("string_2:", string_2)

string_3 = """I went to a restaurant
            yesterday. """
print("string_3:", string_3)



print("""
----------------------------------------------

SIZE

Syntax:

   size = len(string)

Example:
""")

a_string = "Hello world"
print("Number of characters in a_string:", len(a_string))


print(r"""
----------------------------------------------

ESCAPE SEQUENCE

  commonly used escape sequences:

          newline           \n
          tab               \t
          single quote      \'
          double quote      \"

Example:
""")


a_string = "Sincerely,\nPeter Ramsay\nTel:\t(514) 889-3496"
print(a_string)


print(r"""
----------------------------------------------

RAW STRING

  Like normal string with escape sequence ignored.

Syntax:

  string = r'\tstring\tvalue\n'

Example:
""")


a_string = r"Sincerely,\nPeter Ramsay\nTel:\t(514) 889-3496"
print(a_string)


print("""
----------------------------------------------

STRING FORMATTING

    A way to construct a string.

Syntax:

 A) Relative position

    string = "{} {}".format(variable_1, variable_2)

 B) Position

    string = "{0} {1}".format(variable_1, variable_2)

 C) Keyword
    string = "{identifier_1} {identifier_2}".format(identifier_1=variable_1,
               identifier_2="variable_2)

Example:
""")


string = "{} {}".format("Hello", "World")
print("string:", string)

string_2 = "{0} {0} {0} {1}".format("Hello", "World")
print("string_2:", string_2)

string_3 = "{intro} {outro}".format(intro="Hi", outro="good bye")
print("string_3:", string_3)

print("""
----------------------------------------------

STRING CONCATENATION

Syntax:

 final_string = string1 + string2

Example:
""")

string_1 = "Hello"
string_2 = " World"
string_3 = string_1 + string_2
print(string_3)



print("""
----------------------------------------------

REMOVE LEADING AND TRAILING WHITE SPACE

Syntax:

    result = a_string.strip()

Example:
""")

string = " hi "
print(string + string)

new_string = string.strip()
print(new_string + new_string)


print("""
----------------------------------------------

FIND CHARACTER/STRING IN STRING

Syntax:

    index = some_string.find(string)

Note:

    Character count starts from 0

Example:
""")

string = "Hi guys"
substring = "guy"

print("Substring '{substring}' was found at index '{index}' of string '{string}'".format(
    substring=substring, index=string.find(substring), string=string
))


print("""
----------------------------------------------

REPLACEMENT

    Replace all occurrence of a string.

Syntax:

    new_string = string.replace(string_to_replace, string_replacement)

Example:
""")

string = "idealistic"
to_replace = "listic"
replacement = "l"

print("string:", string)
print("Replace {to_replace} by {replacement}".format(to_replace=to_replace, replacement=
                                                     replacement))
new_string = string.replace(to_replace, replacement)
print("new_string:", new_string)
















































#
# # catch empty string
# empty_string = ""
# print("From string: ", empty_string)
# if not empty_string:
#     print("It is a empty string")
#
#
# # string to byte
# 'data'.encode('utf-8')































