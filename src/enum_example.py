from enum import Enum

print("""
----------------------------------------------

ENUM

    Define a set of constants

----------------------------------------------
\n\n\n""")



print("""
----------------------------------------------

CREATE

Syntax:

    class EnumName(Enum):
        Constant_Name_1 = integer
        Constant_Name_2 = integer
        Constant_Name_n = integer

Example:
""")


class Color(Enum):
    Red = 1
    Blue = 2
    Green = 3

print(Color)
print(Color.Red)



print("""
----------------------------------------------

FETCH ITEM

Syntax:

    name = EnumName.Constant_Name.name
    value = EnuName.Constant_Name.value

Example:
""")



print("Integer value {value} represents {color}".format(value=Color.Blue.value,
                                                        color=Color.Blue.name))



print("""
----------------------------------------------

COMPARE

Syntax:

    EnumName.ConstantName

Example:
""")

color = Color.Blue

if color == Color.Blue:
    print('Use color blue')
elif color == Color.Green:
    print('Use color green')
elif color == Color.Red:
    print('Use color red')


print("""
----------------------------------------------

CONVERT INT TO ENUM

Syntax:

    EnumItem = EnumName(Integer)

Example:
""")


color = Color(3)
print(color)























































