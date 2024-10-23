from math import floor
def decimal_to_binary(num: int)->str:
    new_num = num
    binary_digits = []
    while new_num>0:
        rem = new_num%2
        new_num = floor(new_num/2)
        binary_digits.append(rem)

    print(binary_digits)
    number = list(reversed(binary_digits))
    return number

# test
# y = decimal_to_binary(18)

# print(y)

    


