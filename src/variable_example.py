# print("""
# ----------------------------------------------
#
# ASSIGN VALUE TO VARIABLE
#
# Syntax:
#
#     variable_identifier = value
#
# Example:
# """)
# name = "peter"
# print('name = "peter"')
# print("value", name)































# print("""
# ----------------------------------------------
#
# MULTIPLE ASSIGNMENT
#
# Syntax:
#
#     variable_identifier_1 = variable_identifier_2 = value
#
# Note:
#
#     variable_identifier_1 and variable_identifier_2
#     contains the same value
#
# Example:
# """)
# student_1 = student_2 = "peter"
# print('student_1:', student_1)
# print('student_2:', student_2)









































# print("""
# ----------------------------------------------
#
# MULTIPLE ASSIGNMENT
#
# Syntax:
#
#     variable_identifier_1, variable_identifier_2 = value_1, value_2
#
# Note:
#
#     variable_identifier_1 stores value_1
#     variable_identifier_2 stores value_2
#
# Example:
# """)
#
# name, identification = "peter", 9690434
# print('name:', name)
# print('identification:', identification)







































# print("""
# ----------------------------------------------
#
# BUILT IN DATA TYPE
#
#     Data stored in memory can be of many types.
#     Python offers the following data types:
#
#     Numbers
#         int
#         float
#         complex
#     String
#     List
#     Tuple
#     Dictionary
#
# Example:
# """)
#
# integer_number = 10
# print("int: value->{integer} type->{type}".format(integer=integer_number, type=type(integer_number)))
# print()
#
# float_number = 5.6
# print("float: value->{float_num} type->{type}".format(float_num=float_number, type=type(float_number)))
# print()
#
# complex_number = 5j
# print("complex: value->{complex_num} type->{type}".format(complex_num=complex_number, type=type(complex_number)))
# print()
#
# string = "5"
# print("string: value->{str} type->{type}".format(str=string, type=type(string)))
# print()
#
# a_list = [1, 2, 3]
# print("list: value->{list} type->{type}".format(list=a_list, type=type(a_list)))
# print()
#
# a_tuple = (4, 5, 6)
# print("tuple: value->{tuple} type->{type}".format(tuple=a_tuple, type=type(a_tuple)))
# print()
#
# a_dict = {"1": "one", "2": "two"}
# print("dict: value->{dict} type->{type}".format(dict=a_dict, type=type(a_dict)))














































def print_data_type_conversion_proof(to_convert, converted):

    def convert_type_to_phrase(data):
        the_type = type(data)
        if the_type == int:
            return "int number"
        elif the_type == float:
            return "float number"
        elif the_type == complex:
            return "complex number"
        elif the_type == str:
            return "string"
        elif the_type == tuple:
            return "tuple"
        elif the_type == list:
            return "list"

    to_convert_type = convert_type_to_phrase(to_convert)
    converted_type = convert_type_to_phrase(converted)
    print("Given {to_convert_type} '{to_convert_value}' converted to {converted_type} gives you value '{value}' and data type '{type}'".format(
        to_convert_type=to_convert_type,
        to_convert_value=to_convert,
        converted_type=converted_type,
        value=converted,
        type=type(converted)))



print("""
----------------------------------------------

DATA TYPE CONVERSION

    Changes a variable from one data type to another.

Syntax:

        result = built_in_data_type(data)

where
                built_in_data_type         data type name
               ------------------------------------------------
                    int                     integer number
                    float                   float number
                    complex                 complex number
                    str                     string
                    tuple                   tuple
                    list                    list
                    dict                    dictionary

Example:
""")

print("""
Given the following:
given_integer_number = 10
given_float_number = 5.6
given_list = [1, 2, 3]
given_tuple = (4, 5, 6)
""")

given_integer_number = 10
given_float_number = 5.6
given_list = [1, 2, 3]
given_tuple = (4, 5, 6)


integer_number = int(given_float_number)
print_data_type_conversion_proof(to_convert=given_float_number, converted=integer_number)


float_number = float(given_integer_number)
print_data_type_conversion_proof(to_convert=given_integer_number, converted=float_number)


complex_number = complex(given_integer_number)
print_data_type_conversion_proof(to_convert=given_integer_number, converted=complex_number)


string = str(given_integer_number)
print_data_type_conversion_proof(to_convert=given_integer_number, converted=string)


a_list = list(given_tuple)
print_data_type_conversion_proof(to_convert=given_tuple, converted=a_list)


a_tuple = tuple(given_list)
print_data_type_conversion_proof(to_convert=given_list, converted=a_tuple)





















