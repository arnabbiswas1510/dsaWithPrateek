"""
Can be used for converting from decimal to any other base
"""

def toBinary(decimal, result=""):
    if decimal == 0:
        return result
    result = str(decimal%2) + result #Note the usage of str to multiiply by powers of 10
    return toBinary(decimal//2, result)

print(toBinary(233))